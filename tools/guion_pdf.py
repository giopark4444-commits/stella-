#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el PDF del guion desde el markdown canónico.

    guion/GUION_P1_v2.md  →  guion/render/GUION_P1_v2.pdf

Usa el Chrome del sistema en modo headless para imprimir. Los números de página
los pone el pie de Chrome (`--print-to-pdf-header-footer` no acepta plantilla por
CLI), así que se dibujan con un contador CSS propio en cada portadilla de acto y,
para el folio corrido, se deja el pie nativo desactivado y se numeran las escenas.

Uso:
    python3 tools/guion_pdf.py            # genera el PDF
    python3 tools/guion_pdf.py --abrir    # lo genera y lo abre
"""
import argparse
import html as H
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from genweb_guion import cuerpo_desde_md  # noqa: E402  (misma conversión que la web)

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / "guion" / "GUION_P1_v2.md"
SALIDA_DIR = RAIZ / "guion" / "render"
HTML_TMP = SALIDA_DIR / "_guion_print.html"
PDF = SALIDA_DIR / "GUION_P1_v2.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VERSION = "v2.7"

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 24mm; }

* { box-sizing: border-box; }

body {
  font: 11.5pt/1.55 "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  color: #14100e;
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ── portada ── */
.portada {
  height: 247mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  page-break-after: always;
}
.portada .eyebrow {
  font-family: -apple-system, "Helvetica Neue", sans-serif;
  font-size: 8.5pt; letter-spacing: .32em; text-transform: uppercase;
  color: #8a7f76; margin-bottom: 22mm;
}
.portada h1 {
  font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  font-size: 34pt; font-weight: 400; letter-spacing: .06em; margin: 0;
}
.portada .sub { font-size: 15pt; color: #5d534c; margin-top: 5mm; font-style: italic; }
.portada .meta {
  margin-top: 34mm; font-family: -apple-system, "Helvetica Neue", sans-serif;
  font-size: 9pt; color: #8a7f76; line-height: 2;
}
.portada .regla { width: 26mm; border-top: 1px solid #c9bfb6; margin: 12mm 0; }

/* ── actos ── */
h1 {
  page-break-before: always;
  page-break-after: avoid;
  font-family: -apple-system, "Helvetica Neue", sans-serif;
  font-size: 13pt; font-weight: 700; letter-spacing: .22em; text-transform: uppercase;
  text-align: center; margin: 28mm 0 14mm; color: #14100e;
}
h1:first-of-type { page-break-before: avoid; }

/* ── escenas ── */
h2.scene {
  page-break-after: avoid;
  page-break-inside: avoid;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 10pt; font-weight: 700; text-transform: uppercase; letter-spacing: .02em;
  margin: 9mm 0 4mm; padding-bottom: 1.5mm;
  border-bottom: .5pt solid #d6cdc4;
}
h2.h2 {
  page-break-before: always;
  font-family: -apple-system, "Helvetica Neue", sans-serif;
  font-size: 11pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
  margin: 0 0 6mm;
}

hr { display: none; }

p.action { margin: 0 0 3.4mm; text-align: left; orphans: 2; widows: 2; }
/* aire al volver de un bloque de diálogo a la acción */
div + p.action { margin-top: 5mm; }

/* ── diálogo ── */
.cue {
  page-break-after: avoid;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 10pt; font-weight: 700; letter-spacing: .08em;
  margin: 4.5mm 0 0 62mm;
}
.paren {
  page-break-after: avoid;
  font-style: italic; color: #6b615a; font-size: 10.5pt;
  margin: .3mm 0 0 50mm;
}
.dlg { margin: .3mm 38mm 0 38mm; orphans: 2; widows: 2; }

/* ── notas y remates ── */
p:not([class]) {
  font-size: 10pt; font-style: italic; color: #6b615a;
  border-left: 2pt solid #ded5cc; padding-left: 4mm; margin: 4mm 0;
}
.foot { display: none; }

strong { font-weight: 700; }
em { font-style: italic; }
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--abrir", action="store_true", help="abre el PDF al terminar")
    args = ap.parse_args()

    if not Path(CHROME).exists():
        raise SystemExit(f"✗ no encuentro Chrome en {CHROME}")

    SALIDA_DIR.mkdir(parents=True, exist_ok=True)
    cuerpo = cuerpo_desde_md(MD.read_text(encoding="utf-8"))

    portada = f"""<section class="portada">
<p class="eyebrow">Película 1 de la saga</p>
<h1>STELLA</h1>
<p class="sub">a falling star</p>
<div class="regla"></div>
<p class="meta">Guion &middot; borrador de producción {VERSION}<br>
{len(re.findall(r'<h2 class="scene">', cuerpo))} secuencias &middot; 3 actos<br>
{date.today().strftime('%d.%m.%Y')}</p>
</section>"""

    doc = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        f"<title>Stella Fugaz · Guion {VERSION}</title><style>{CSS}</style></head>"
        f"<body>{portada}{cuerpo}</body></html>"
    )
    HTML_TMP.write_text(doc, encoding="utf-8")

    # Chrome headless ESCRIBE el PDF y después se queda colgado sin salir (con perfil
    # propio y el Chrome del usuario abierto). Así que no esperamos al proceso:
    # esperamos al archivo, comprobamos que dejó de crecer, y lo cerramos nosotros.
    PDF.unlink(missing_ok=True)
    perfil = tempfile.mkdtemp(prefix="chrome-guion-")
    proc = subprocess.Popen(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--user-data-dir={perfil}", f"--print-to-pdf={PDF}", HTML_TMP.as_uri()],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        limite = time.monotonic() + 600
        estable = 0
        anterior = -1
        while time.monotonic() < limite:
            time.sleep(2)
            if proc.poll() is not None and not PDF.exists():
                raise SystemExit("✗ Chrome terminó sin escribir el PDF")
            tam = PDF.stat().st_size if PDF.exists() else 0
            if tam and tam == anterior:
                estable += 1
                if estable >= 3:          # 6 s sin crecer = terminado
                    break
            else:
                estable = 0
            anterior = tam
        else:
            raise SystemExit("✗ Chrome no escribió el PDF en 10 min")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
        shutil.rmtree(perfil, ignore_errors=True)

    if not PDF.exists() or PDF.stat().st_size < 20_000:
        raise SystemExit("✗ el PDF salió vacío o demasiado pequeño")

    print(f"✓ {PDF.relative_to(RAIZ)}  ({PDF.stat().st_size/1024:.0f} KB)")
    HTML_TMP.unlink(missing_ok=True)

    if args.abrir:
        subprocess.run(["open", str(PDF)], check=False)


if __name__ == "__main__":
    main()
