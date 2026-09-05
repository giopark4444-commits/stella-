#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cambia la COLA DE ESTILO de los prompts de concepto (las tres MINI).

La cola es la última frase de cada prompt — lo único que dice cómo debe verse.
Se cambia sola, de un tirón, para poder probar estilos sin tocar los conceptos.

    python3 tools/cola_estilo.py                       # muestra la cola actual
    python3 tools/cola_estilo.py --set "Otra cosa."    # la cambia
    python3 tools/cola_estilo.py --restore             # vuelve a "Hand-painted anime."

Ojo: si un estilo empieza a rebotar por propiedad intelectual, esto es lo primero
que hay que apagar. `tools/estilo_canon.py --check` NO detecta variantes mal
escritas a propósito (p. ej. «Ghibly» en vez de «Ghibli»).
"""
import argparse
import re
from pathlib import Path

GUION = Path(__file__).resolve().parent.parent / "guion" / "03_prompts"
ARCHIVOS = [
    "PROMPTS_LOCACIONES_MINI.md",
    "PROMPTS_PERSONAJES_MINI.md",
    "PROMPTS_DISENOS_MINI.md",
]
POR_DEFECTO = "Hand-painted anime."

# La cola es todo lo que va después del último "Show me 4 examples." (y de los
# desvíos que puedan venir detrás). Se detecta como la última oración de la línea.
RE_PROMPT = re.compile(r"^(How would .*?)([^.!?]*\.)\s*$")


def cola_actual(texto: str) -> set[str]:
    colas = set()
    for linea in texto.splitlines():
        m = RE_PROMPT.match(linea)
        if m:
            colas.add(m.group(2).strip())
    return colas


def cambia(texto: str, nueva: str) -> tuple[str, int]:
    n = 0
    fuera = []
    for linea in texto.splitlines():
        m = RE_PROMPT.match(linea)
        if m:
            cabeza = m.group(1).rstrip()
            fuera.append(f"{cabeza} {nueva}")
            n += 1
        else:
            fuera.append(linea)
    return "\n".join(fuera) + ("\n" if texto.endswith("\n") else ""), n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", dest="nueva", help="la nueva cola de estilo (con punto final)")
    ap.add_argument("--restore", action="store_true", help=f'vuelve a "{POR_DEFECTO}"')
    args = ap.parse_args()

    nueva = POR_DEFECTO if args.restore else args.nueva

    if not nueva:
        for nombre in ARCHIVOS:
            colas = cola_actual((GUION / nombre).read_text(encoding="utf-8"))
            print(f"{nombre:<32} {' / '.join(sorted(colas)) or '(ninguna)'}")
        return

    if not nueva.endswith((".", "!", "?")):
        nueva += "."

    total = 0
    for nombre in ARCHIVOS:
        p = GUION / nombre
        texto = p.read_text(encoding="utf-8")
        nuevo, n = cambia(texto, nueva)
        p.write_text(nuevo, encoding="utf-8")
        print(f"  {nombre:<32} {n} prompts")
        total += n

    print(f"\n✓ {total} prompts con la cola: «{nueva}»")


if __name__ == "__main__":
    main()
