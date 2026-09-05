#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los DOS entregables versionados a partir del guion de trabajo.

  guion/GUION_CLASICO_vX.Y.md      · para leer  (nombres normales)
  guion/GUION_REFERENCIAS_vX.Y.md  · para promptear (@tags de la biblioteca)

Se regeneran siempre desde la fuente, asi que no pueden desincronizarse.
Correr DESPUES de tools/gentags.py.
"""
import io, re, pathlib, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "guion" / "02_guiones" / "GUION_P1_v2.md"
TAGS   = RAIZ / "guion" / "02_guiones" / "GUION_P1_v2_TAGS.md"

src = io.open(FUENTE, encoding="utf-8").read()
m = re.search(r"Película 1 \((v[\d.]+)\)", src)
if not m:
    sys.exit("no encuentro la version en la cabecera de %s" % FUENTE.name)
V = m.group(1)

CAB_CLASICO = """# STELLA · *a falling star*
## Guion clásico — Película 1 · **{v}**

> 📖 **Esta es la versión para leer.** Nombres normales, sin etiquetas.
> Para producir prompts usa `GUION_REFERENCIAS_{v}.md`, que trae los `@tags` de la biblioteca.
> ⚠️ Generado automáticamente desde `GUION_P1_v2.md`. **No editar a mano.**
"""

CAB_REFS = """# STELLA · *a falling star*
## Guion de referencias — Película 1 · **{v}**

> 🏷️ **Esta es la versión para promptear.** Cada nombre viene sustituido por su `@tag` de la
> biblioteca, y **el tag cambia según la secuencia** (Stella tiene once estados, Vera ocho,
> Selka nueve).
> Cada `## SEC` abre con las líneas 🏷️ de **locación**, **reparto** y **props**.
> Para leer la historia usa `GUION_CLASICO_{v}.md`.
> ⚠️ Generado automáticamente desde `GUION_P1_v2.md`. **No editar a mano.**
"""

def corta_cabecera(t):
    """Quita las dos primeras lineas de titulo y el bloque > que las sigue."""
    lineas = t.split("\n")
    i = 0
    while i < len(lineas) and (lineas[i].startswith("#") or lineas[i].startswith(">")
                               or not lineas[i].strip()):
        i += 1
        if i > 40:
            break
    return "\n".join(lineas[i:]).lstrip("\n")

sal = []
for cab, cuerpo, nombre in (
    (CAB_CLASICO, src, "GUION_CLASICO_%s.md" % V),
    (CAB_REFS, io.open(TAGS, encoding="utf-8").read(), "GUION_REFERENCIAS_%s.md" % V),
):
    txt = cab.format(v=V) + "\n" + corta_cabecera(cuerpo) + "\n"
    p = RAIZ / "guion" / "02_guiones" / nombre
    io.open(p, "w", encoding="utf-8").write(txt)
    secs = txt.count("\n## SEC")
    assert secs == 40, "%s tiene %d secuencias, esperaba 40" % (nombre, secs)
    sal.append((nombre, len(txt), secs))

for n, b, s in sal:
    print("  ✓ %-34s %9s bytes · %d secuencias" % (n, "{:,}".format(b), s))
print("\nversion detectada: %s" % V)
