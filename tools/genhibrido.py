#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el guion híbrido desde el markdown canónico.

    guion/GUION_P1_v2.md  +  tools/dialogos_en.json  →  guion/GUION_P1_v2_DIALOGOS_EN.md

Híbrido = **todo en español** (encabezados, acción, acotaciones, nombres de personaje)
y **solo lo que se dice en voz alta, en inglés**.

El diccionario `tools/dialogos_en.json` mapea cada línea hablada en español a su
traducción. Si aparece una línea nueva en el guion y no está en el diccionario,
el script **falla y te la lista** en vez de publicar un híbrido a medias.

Uso:
    python3 tools/genhibrido.py            # informe (dry-run)
    python3 tools/genhibrido.py --apply    # escribe el .md y el .html
    python3 tools/genhibrido.py --faltan   # solo lista lo que falta traducir
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from genweb_guion import es_cue  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / "guion" / "GUION_P1_v2.md"
DIC = Path(__file__).resolve().parent / "dialogos_en.json"
SALIDA_MD = RAIZ / "guion" / "GUION_P1_v2_DIALOGOS_EN.md"
SALIDA_HTML = RAIZ / "guion" / "GUION_P1_v2_DIALOGOS_EN.html"
VERSION = "v2.7"

CABECERA = f"""# STELLA FUGAZ · "EL NODO DE ERDIA"
## Guion — Película 1 ({VERSION}) · Acción en español · Diálogos en inglés

> **Versión híbrida.** Todo en español —encabezados, acción, acotaciones y nombres de personaje—
> y **solo lo que los personajes dicen en voz alta, en inglés**.
> Generado desde `GUION_P1_v2.md` con `tools/genhibrido.py`. **No editar a mano:**
> corrige el guion canónico (o el diccionario `tools/dialogos_en.json`) y vuelve a generar.

"""


def recorre(md: str):
    """Itera (linea, es_dialogo_hablado)."""
    en_dialogo = False
    for cruda in md.splitlines():
        l = cruda.strip()
        if not l:
            en_dialogo = False
            yield cruda, False
            continue
        if l.startswith("#") or l == "---" or l.startswith("> "):
            en_dialogo = False
            yield cruda, False
            continue
        if es_cue(l):
            en_dialogo = True
            yield cruda, False
            continue
        if en_dialogo and re.fullmatch(r"\*\(.*\)\*", l):   # acotación: se queda en español
            yield cruda, False
            continue
        yield cruda, en_dialogo


def genera(md: str, dic: dict) -> tuple[str, list[str]]:
    fuera, faltan = [], []
    # saltar la cabecera del canónico (hasta el primer "# ACTO")
    cuerpo = md[md.index("# ACTO"):]
    for linea, hablado in recorre(cuerpo):
        if hablado:
            l = linea.strip()
            if l in dic:
                fuera.append(dic[l])
            else:
                faltan.append(l)
                fuera.append(linea)
        else:
            fuera.append(linea)
    return CABECERA + "\n".join(fuera).rstrip() + "\n", faltan


def a_html(md_hibrido: str, plantilla: Path) -> str:
    """Reusa el chasis del HTML del guion, cambiando solo el cuerpo."""
    from genweb_guion import cuerpo_desde_md
    base = plantilla.read_text(encoding="utf-8")
    prefijo, resto = base.split('<div class="wrap">', 1)
    _, sufijo = resto.split("<script>", 1)
    prefijo = re.sub(r"GUION v[\w.]+", f"HÍBRIDO {VERSION}", prefijo)
    prefijo = prefijo.replace("Stella Fugaz · Guion completo",
                              "Stella Fugaz · Guion híbrido (diálogos en inglés)")
    pie = f'<p class="foot">Stella Fugaz · El Nodo de Erdia · híbrido {VERSION}</p>'
    return (prefijo + '<div class="wrap">\n' + cuerpo_desde_md(md_hibrido)
            + "\n" + pie + "\n</div>\n<script>" + sufijo)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="escribe el .md y el .html")
    ap.add_argument("--faltan", action="store_true", help="solo lista lo que falta traducir")
    args = ap.parse_args()

    md = MD.read_text(encoding="utf-8")
    dic = json.loads(DIC.read_text(encoding="utf-8"))
    hibrido, faltan = genera(md, dic)

    if faltan:
        print(f"✗ faltan {len(faltan)} líneas por traducir en tools/dialogos_en.json:\n")
        for l in faltan:
            print(f'  "{l}": "",')
        raise SystemExit(1)

    if args.faltan:
        print("✓ no falta ninguna línea por traducir")
        return

    total = sum(1 for _, h in recorre(md[md.index('# ACTO'):]) if h)
    print(f"diccionario : {len(dic)} líneas")
    print(f"híbrido     : {total} diálogos traducidos · {len(hibrido):,} bytes")

    if args.apply:
        SALIDA_MD.write_text(hibrido, encoding="utf-8")
        SALIDA_HTML.write_text(
            a_html(hibrido, RAIZ / "guion" / "GUION_WEB.html"), encoding="utf-8")
        print(f"✓ {SALIDA_MD.name} y {SALIDA_HTML.name} escritos")
    else:
        print("(dry-run: nada escrito; usa --apply)")


if __name__ == "__main__":
    main()
