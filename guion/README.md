# 🗂️ Mapa de `guion/`

Los 144 archivos que antes estaban sueltos aquí ahora están agrupados **por función**.
No se borró ni se renombró nada: solo se movieron. El historial de git conserva cada archivo.

| Carpeta | Qué contiene | Nº |
|---|---|---|
| `01_historia/` | Desarrollo narrativo: escaletas, personajes, mundo, tratamientos, beat sheet, continuidad, material de la trilogía | 24 |
| `02_guiones/` | Los guiones propiamente dichos: `GUION_P1_v2.md` (**fuente de verdad**), los entregables versionados, versiones EN, técnico y guiones antiguos `PELI1_*` | 15 |
| `03_prompts/` | Todos los `PROMPTS_*` en `.md` / `.txt` / `.csv` (imagen, storyboard, locaciones, personajes, diseños) | 50 |
| `04_produccion/` | Hojas de producción, bloques de 20 s, clips por acto, checklist, timings | 15 |
| `05_referencias/` | Mapeo de referencias visuales y `TAGS.md` | 4 |
| `06_web/` | Entregables HTML navegables, incluido `SEEDANCE_INDEX.html` | 36 |
| `render/` | PDF y documentos de render — *ya estaba organizada, no se tocó* | — |
| `estructura/` | Script de creación de estructura — *no se tocó* | — |
| `_archivo_guion_v1/` | Respaldo congelado del guion v1 (2026-06-27) — *no se tocó* | — |

## ⚠️ Al mover cambiaron dos cosas

1. **Las URLs públicas de los HTML.** Lo que antes era
   `…/stella-/guion/STORYBOARD.html` ahora es `…/stella-/guion/06_web/STORYBOARD.html`.
   Los puntos de entrada **no cambiaron**: `index.html` y `STELLA_FUGAZ.html` siguen en la raíz,
   y todos sus enlaces internos están actualizados.
2. **Las rutas dentro de `tools/`.** Los ocho generadores ya apuntan a las carpetas nuevas y
   están verificados: `estilo_canon.py --check`, `genweb_guion.py`, `genhibrido.py`,
   `seedance_safe.py --check` y `cola_estilo.py` corren sin error.

La cadena de generación no cambió de orden — sigue como está en `RETOMAR-AQUI.md`.
