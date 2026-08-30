#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenera la web del guion desde el markdown canónico.

    guion/GUION_P1_v2.md  →  guion/GUION_WEB.html  →  pestaña "Guion" de STELLA_FUGAZ.html

Uso:
    python3 tools/genweb_guion.py            # informe (dry-run)
    python3 tools/genweb_guion.py --apply    # escribe los cambios

La variante SEEDANCE (GUION_WEB_SEEDANCE.html) NO se genera aquí:
la produce `tools/seedance_safe.py --apply` a partir del HTML normal.
Correr seedance_safe DESPUÉS de este script.
"""
import argparse
import html as H
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / "guion" / "GUION_P1_v2.md"
WEB = RAIZ / "guion" / "GUION_WEB.html"
APP = RAIZ / "STELLA_FUGAZ.html"
VERSION = "v2.6"

CUE_RE = re.compile(r"^\*\*(.+)\*\*$")


def en_linea(texto: str) -> str:
    """Negritas y cursivas de markdown → strong/em, con escape HTML."""
    texto = H.escape(texto, quote=False)
    texto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(r"\*(.+?)\*", r"<em>\1</em>", texto)
    return texto


def es_cue(linea: str) -> bool:
    """¿La línea es SOLO un nombre de personaje en negrita? (**VERA (CONT.)**)"""
    m = CUE_RE.match(linea.strip())
    if not m:
        return False
    nucleo = re.sub(r"\(.*?\)", "", m.group(1))          # fuera el paréntesis
    nucleo = re.sub(r"[\"“”'…\.,:·-]", "", nucleo).strip()
    return bool(nucleo) and nucleo == nucleo.upper()


def cuerpo_desde_md(md: str) -> str:
    lineas = md.splitlines()
    fuera: list[str] = []
    i = 0
    en_dialogo = False

    # saltar cabecera: título + blockquote de convenciones, hasta el primer "# ACTO"
    while i < len(lineas) and not lineas[i].startswith("# ACTO"):
        i += 1

    while i < len(lineas):
        cruda = lineas[i]
        linea = cruda.strip()

        if not linea:
            en_dialogo = False
            i += 1
            continue

        if linea.startswith("# "):                       # acto
            fuera.append(f"<h1>{en_linea(linea[2:])}</h1>")
            en_dialogo = False
        elif linea.startswith("## SEC"):                 # escena
            fuera.append(f'<h2 class="scene">{en_linea(linea[3:])}</h2>')
            en_dialogo = False
        elif linea.startswith("## "):                    # otras h2 (notas P2)
            fuera.append(f'<h2 class="h2">{en_linea(linea[3:])}</h2>')
            en_dialogo = False
        elif linea == "---":
            fuera.append("<hr>")
            en_dialogo = False
        elif linea.startswith("> "):                     # nota citada (montaje intercalado)
            fuera.append(f"<p>{en_linea(linea[2:])}</p>")
            en_dialogo = False
        elif es_cue(linea):
            fuera.append(f'<div class="cue">{H.escape(CUE_RE.match(linea).group(1), quote=False)}</div>')
            en_dialogo = True
        elif en_dialogo and re.fullmatch(r"\*\(.*\)\*", linea):
            fuera.append(f'<div class="paren">{H.escape(linea[1:-1], quote=False)}</div>')
        elif en_dialogo:
            fuera.append(f'<div class="dlg">{en_linea(linea)}</div>')
        else:
            fuera.append(f'<p class="action">{en_linea(linea)}</p>')

        i += 1

    return "\n".join(fuera)


def regenerar_web(md: str, web_actual: str) -> str:
    prefijo, resto = web_actual.split('<div class="wrap">', 1)
    _, sufijo = resto.split("<script>", 1)
    prefijo = re.sub(r"GUION v[\w.]+", f"GUION {VERSION}", prefijo)
    pie = f'<p class="foot">Stella Fugaz · El Nodo de Erdia · Película 1 · guion {VERSION}</p>'
    return (
        prefijo
        + '<div class="wrap">\n'
        + cuerpo_desde_md(md)
        + "\n" + pie + "\n</div>\n<script>"
        + sufijo
    )


def escapar_srcdoc(doc: str) -> str:
    return doc.replace("&", "&amp;").replace('"', "&quot;")


def parchear_app(app_html: str, guion_web: str) -> str:
    """Reemplaza el srcdoc del iframe cuyo título es 'Guion completo'."""
    marcador = escapar_srcdoc("<title>Stella Fugaz · Guion completo</title>")
    for m in re.finditer(r'(<iframe[^>]*srcdoc=")', app_html):
        ini = m.end()
        fin = app_html.index('"', ini)
        if marcador in app_html[ini:fin]:
            return app_html[:ini] + escapar_srcdoc(guion_web) + app_html[fin:]
    raise SystemExit("✗ no encontré el iframe del guion en STELLA_FUGAZ.html")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="escribe los cambios en disco")
    args = ap.parse_args()

    md = MD.read_text(encoding="utf-8")
    web_actual = WEB.read_text(encoding="utf-8")
    nuevo_web = regenerar_web(md, web_actual)

    app_actual = APP.read_text(encoding="utf-8")
    nueva_app = parchear_app(app_actual, nuevo_web)

    print(f"GUION_WEB.html      {len(web_actual):>9,} → {len(nuevo_web):>9,} bytes")
    print(f"STELLA_FUGAZ.html   {len(app_actual):>9,} → {len(nueva_app):>9,} bytes")

    # sanidad mínima: las escenas nuevas deben estar en el HTML
    for marca in ("SEC. 0 ", "SEC. 12A", "SEC. 20A", "SEC. 20B", "SEC. 20C", "SEC. 20D",
                  "LOS AÑOS", "PUERTO ESTELAR", "AÑO 20", "CELDAS DEL NIVEL DE SERVICIO",
                  "SALA DE ENTRENAMIENTO"):
        if marca not in nuevo_web:
            raise SystemExit(f"✗ sanidad: falta «{marca}» en el HTML generado")
    print("✓ sanidad OK (12A · 20A/B/C/D · montaje · puerto · AÑO 20 · celdas · sala · apertura en frío)")

    if args.apply:
        WEB.write_text(nuevo_web, encoding="utf-8")
        APP.write_text(nueva_app, encoding="utf-8")
        print("✓ escrito en disco")
    else:
        print("(dry-run: nada escrito; usa --apply)")


if __name__ == "__main__":
    main()
