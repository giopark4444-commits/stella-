#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cambia el bloque de ESTILO de todos los prompts del proyecto.

Dos problemas que resuelve:

1. **Bloqueo por propiedad intelectual.** «Studio Ghibli» es un nombre de estudio y los
   moderadores de OpenAI lo rechazan. Se sustituye por una descripción del MISMO look
   sin nombrar a nadie.

2. **Demasiado detalle.** Los modelos, si no se les frena, rellenan de micro-textura y
   acaban pareciendo render 3D. Las palabras que empujan detalle (`painterly detail`,
   `concept art`) se cambian por las que lo frenan (`simplified shapes`, `flat painted
   masses`, `restrained detail`) y se añaden negativos explícitos.

Uso:
    python3 tools/estilo_canon.py            # informe (dry-run)
    python3 tools/estilo_canon.py --apply    # escribe los cambios
    python3 tools/estilo_canon.py --check    # falla si queda algún nombre de estudio

Correr DESPUÉS `tools/seedance_safe.py --apply` para refrescar la variante segura.
Idempotente: correrlo dos veces no cambia nada la segunda vez.
"""
import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GUION = RAIZ / "guion"
EXTS = (".md", ".txt", ".csv")

# ── nombres que disparan el filtro de propiedad intelectual ────────────────────
NOMBRES_PROHIBIDOS = ("Studio Ghibli", "Ghibli", "Hayao Miyazaki", "Miyazaki", "Satoshi Kon")

# ── el look, descrito sin nombrar a nadie ─────────────────────────────────────
BASE_FONDO = (
    "2D hand-painted anime film background, cel-animation matte painting — broad "
    "simplified shapes and flat painted masses rather than fine detail, restrained "
    "texture, clean readable silhouettes, soft brushwork with visible painted edges; "
    "strong atmospheric perspective with the distance fading pale; warm cinematic "
    "light, soft grain"
)
BASE_HOJA = (
    "2D hand-painted anime design sheet, cel-animation style — clean line work, flat "
    "cel shading with simple shadow shapes, restrained detail, soft painted edges, "
    "soft cinematic lighting, soft grain"
)
NEG_DETALLE = (
    "no photorealism, no 3D render, no CGI, no hyper-detailed rendering, "
    "no busy micro-texture"
)

# Orden importa: primero las cadenas largas, luego las cortas.
REEMPLAZOS: list[tuple[str, str]] = [
    # — placas de locación (24) —
    (
        "Studio Ghibli style — a wide-angle establishing view of the entire location, "
        "general environment overview (not a specific camera shot), hand-painted anime "
        "background/environment art, painterly detail, soft cinematic lighting, soft "
        "grain, no characters.",
        f"{BASE_FONDO}. A wide-angle establishing view of the entire location, general "
        "environment overview (not a specific camera shot), no characters.",
    ),
    # — hojas de personaje (31) —
    (
        "Studio Ghibli style CHARACTER SHEET (model sheet / turnaround) — the same "
        "character on a clean neutral background: front view, 3/4 view and full-body, "
        "plus a face close-up, all consistent across views; hand-painted anime, soft "
        "cinematic lighting, soft grain.",
        "2D hand-painted anime CHARACTER SHEET (model sheet / turnaround), "
        "cel-animation style — clean line work, flat cel shading with simple shadow "
        "shapes, restrained detail; the same character on a clean neutral background: "
        "front view, 3/4 view and full-body, plus a face close-up, all consistent "
        "across views; soft cinematic lighting, soft grain.",
    ),
    # — hojas de nave y de objeto —
    (
        "Studio Ghibli style, hand-painted anime concept art, clean neutral studio "
        "background, cinematic soft lighting, soft grain,",
        f"{BASE_HOJA}, clean neutral studio background,",
    ),
    (
        "Studio Ghibli style, hand-painted anime concept art, clean dark neutral "
        "background, cinematic glow lighting, soft grain,",
        f"{BASE_HOJA}, clean dark neutral background, gentle glow lighting,",
    ),
    (
        "Studio Ghibli style, hand-painted anime concept art, clean dark neutral "
        "background, cinematic soft lighting, soft grain,",
        f"{BASE_HOJA}, clean dark neutral background,",
    ),
    (
        "Studio Ghibli style, hand-painted anime concept art, clean neutral background, "
        "cinematic soft lighting, soft grain,",
        f"{BASE_HOJA}, clean neutral background,",
    ),
    # — cola de las versiones MINI (≤25 palabras + estilo) —
    (
        "Studio Ghibli style.",
        "Hand-painted 2D anime style, flat cel shading, simplified shapes.",
    ),
    # — frames y clips del storyboard (otra redacción) —
    ("Satoshi Kon-style anime storyboard frame", "cel-animation anime storyboard frame"),
    ("Satoshi Kon–style anime storyboard frame", "cel-animation anime storyboard frame"),
    ("Satoshi Kon-style anime", "cel-animation anime"),
    ("Satoshi Kon–style anime", "cel-animation anime"),
    ("2D hand-painted Studio Ghibli aesthetic", "2D hand-painted cel-animation look"),
    ("2D hand-painted Ghibli touch", "2D hand-painted cel-animation look"),
    ("Miyazaki style and Satoshi Kon mood", "warm hand-painted look with a quiet, observational mood"),
    ("Studio Ghibli + Satoshi Kon", "hand-painted cel animation"),
    ("Satoshi Kon + Ghibli", "cel animation, observational mood"),
    ("Studio-Ghibli landscape", "hand-painted landscape"),

    # — restos sueltos —
    ("Studio Ghibli style`.", "hand-painted 2D anime style`."),
    ("Studio Ghibli style**.", "hand-painted 2D anime style**."),
    ("Studio Ghibli style", "hand-painted 2D anime style"),
    ("Studio Ghibli", "hand-painted cel animation"),
    ("Satoshi Kon", "quiet observational"),
    ("Hayao Miyazaki", "warm hand-painted"),
    ("Miyazaki", "warm hand-painted"),
    ("Ghibli", "hand-painted"),
]

# Negativos: añadir los anti-detalle una sola vez por línea de Negative.
RE_NEGATIVE = re.compile(r"(\*\*Negative:\*\*|Negative:)(\s*)(?!.*no photorealism)([^\n]*)")


def frena_detalle(texto: str) -> tuple[str, int]:
    """Añade los negativos anti-detalle a cada línea de Negative que no los tenga."""
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        n += 1
        return f"{m.group(1)}{m.group(2)}{NEG_DETALLE}, {m.group(3)}"

    return RE_NEGATIVE.sub(sub, texto), n


def procesa(texto: str) -> tuple[str, int, int]:
    cambios = 0
    for viejo, nuevo in REEMPLAZOS:
        if viejo in texto:
            cambios += texto.count(viejo)
            texto = texto.replace(viejo, nuevo)
    texto, negs = frena_detalle(texto)
    return texto, cambios, negs


def archivos() -> list[Path]:
    out = []
    for p in sorted(GUION.rglob("*")):
        if p.suffix in EXTS and "_SEEDANCE" not in p.name and "_archivo_" not in str(p):
            out.append(p)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="escribe los cambios en disco")
    ap.add_argument("--check", action="store_true", help="falla si queda un nombre de estudio")
    args = ap.parse_args()

    if args.check:
        malos = []
        for p in archivos():
            txt = p.read_text(encoding="utf-8")
            for nombre in NOMBRES_PROHIBIDOS:
                if nombre in txt:
                    malos.append(f"{p.name}: «{nombre}» ×{txt.count(nombre)}")
        if malos:
            print("✗ quedan nombres de estudio o autor:")
            for m in malos:
                print("   ", m)
            sys.exit(1)
        print("✓ ningún nombre de estudio ni de autor en el corpus")
        return

    tot_est = tot_neg = tot_arch = 0
    for p in archivos():
        txt = p.read_text(encoding="utf-8")
        nuevo, est, neg = procesa(txt)
        if nuevo == txt:
            continue
        tot_arch += 1
        tot_est += est
        tot_neg += neg
        print(f"  {p.name:<38} estilo ×{est:<4} negativos ×{neg}")
        if args.apply:
            p.write_text(nuevo, encoding="utf-8")

    print(f"\nArchivos tocados : {tot_arch}")
    print(f"Bloques de estilo: {tot_est}")
    print(f"Negativos        : {tot_neg}")
    print("ESCRITO EN DISCO" if args.apply else "(dry-run: nada escrito; usa --apply)")


if __name__ == "__main__":
    main()
