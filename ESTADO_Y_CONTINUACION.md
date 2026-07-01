# 📌 ESTADO Y CONTINUACIÓN — Stella Fugaz «El Nodo de Erdia»

> **Documento de traspaso.** Si me abres desde otra sesión/dispositivo, lee esto primero:
> resume el proyecto, el canon, qué está hecho, dónde vive cada cosa y qué falta.
> Última actualización: 2026-07-01 · Commit: `e9da7c1`.

---

## 🎬 El proyecto
- **Película 1** de una saga (2-3 films). Tragedia animada, estilo **Studio Ghibli + Satoshi Kon**, **21:9**.
- **Duración objetivo:** ~48 min · **619 planos** (découpage Ghibli/Kon con planos contemplativos, silencios, ritmo 間/ma).
- La saga se dividió en 3 partes por decisión **narrativa** (sola / sola / dúo), NO porque P1 fuera larga. P1 es lean.
- Logline: una niña huye de su mundo moribundo con la fuente de vida del planeta en la mano, con la promesa de volver, hacerse fuerte y salvar a la hermana que el enemigo le robó.

## 🎨 Canon visual (IMPORTANTE — no equivocarse)
- **Intro:** la superficie de Erdia es **VERDE, sana y viva**, con **UNA grieta pequeña y oscura**. La cámara entra por esa grieta pequeña; al **bajar**, el hueco es enorme y **todo está muerto** (roca gris → caverna negra hueca = `@CorazonMuerto`). La superficie NO es corteza rocosa.
- **Ojos:** Stella y Naio (padre) tienen ojos **ámbar**. Vera, Selka y los de línea materna, **gris-azul**. Noah: pelo oscuro, ojos marrones (NO blanco). Varios secundarios NO son de pelo blanco (Korin, Lessa, pilotos).
- **Gix:** NO humano — axolote de luz (luzagua-azul con puntos dorados).
- **Naiel/naieli** = la especie/pueblo. **Luzagua** = agua-y-luz que brilla.

## 🧩 Prompts de referencia (GPT Image 2 / Higgsfield) — 2 versiones cada uno
Todos empiezan con la orden imperativa dentro del campo/descripción:
- **Locaciones (21):** `Make a location sheet of …`
- **Personajes (31):** `Make a character sheet of …`
- **Naves (6) + Props (11) = 17 objetos:** `Make an object sheet of …`

Dos versiones:
1. **Completa** — con campos (Location/Character/Subject, etc.); prompt copiado compacto (~570 car.).
2. **MINI** — solo la descripción en **≤25 palabras** + `Studio Ghibli style.` (sin campos ni negativos).

## 📁 Dónde vive cada cosa (archivos fuente `guion/*.md`)
| Contenido | Archivo(s) |
|---|---|
| Locaciones (21) completa | `PROMPTS_LOCACIONES.md` |
| Locaciones (21) MINI | `PROMPTS_LOCACIONES_MINI.md` |
| Diseños (48) completa | `PROMPTS_DISENOS.md` (naves+props) · `PROMPTS_PERSONAJES.md` (31) |
| Diseños (48) MINI | `PROMPTS_DISENOS_MINI.md` |
| Storyboard frames GPT Image (619) | `PROMPTS_IMG_ACTO1/2/3.md` |
| Storyboard prompt pages (86) | `PROMPTS_SBPAGES_ACTO1/2/3.md` |
| Prompts de video / clips Seedance (233) | `PROMPTS_SB_ACTO1/2/3.md` |
| Biblias de acto | `PROMPTS_ACTO1/2/3.md` |
| Guion, historia, estructura | `GUION_P1_v2.md`, `PELI1_*`, etc. |

## 🌐 La web (todo navegable con botón copiar)
- **Portada:** `index.html` (raíz).
- **App única (todo embebido):** `STELLA_FUGAZ.html` (raíz, ~7.4 MB). Pestañas: Historia, Storyboard, Guion, Referencias, Prompts, Prompts storyboard, SB Prompt Pages, Frames GPT Image, **Locaciones**, **Locaciones MINI**, **Diseños**, **Diseños MINI**, Guion técnico, Pelis 2 y 3.
- Páginas sueltas: `guion/PROMPTS_*_WEB.html`.
- **Los generadores** (Python) viven en el scratchpad de la sesión, NO en el repo:
  `locweb.py, locmini.py, designweb.py, designmini.py, imgframes.py, sbpages.py, sbprompts.py, onefile.py, storyboard.py, shotlist.py`.
  Flujo: editar `guion/*.md` → correr el generador → regenera el `.html` → `onefile.py` regenera `STELLA_FUGAZ.html`.
  ⚠️ Si me abres en otra sesión, estos scripts hay que **recrearlos** (no están versionados).

## 🖥️ Ramas y despliegue
- Se desarrolla en **`claude/erdia-node-script-review-fc983t`** y se refleja en **`main`** (ambas al mismo commit).
- **GitHub Pages:** pendiente de activar por el usuario → Settings ▸ Pages ▸ Deploy from a branch ▸ **`main`** ▸ `/ (root)`. Link resultante: `https://giopark4444-commits.github.io/stella-/` (y `…/STELLA_FUGAZ.html`).
  - ⚠️ Si el repo es **privado + plan Free**, Pages no publica: hacer repo público o usar Vercel (integración Git).

## 🎞️ Generación de imágenes — estado (IMPORTANTE)
- Cuenta Higgsfield: plan **Ultra**, saldo **~2.74 créditos** (al 2026-07-01).
- **Nano Banana normal es ILIMITADO SOLO en la app web de Higgsfield** (interfaz, logueado).
- **Por la vía MCP/API (como genera el asistente) SÍ cobra:** nano_banana ≈ 1 cr, nano_banana_pro = 2 cr, modelos **Soul** ≈ 0.12 cr, Seedream 4.5 = 1 cr. (Comprobado: una imagen bajó 3.74 → 2.74.)
- **Decisión del usuario:** generar **él mismo en la app** (gratis, ilimitado), copiando los prompts de la web.
- Ajustes: modelo Nano Banana, **21:9** para locaciones/frames, 1:1 o 3:4 para hojas de personaje/objeto.
- Orden sugerido: 1) 21 locaciones → 2) 31 personajes → 3) 17 naves/props → 4) frames adjuntando la hoja correspondiente para consistencia.
- El asistente **no puede** entrar por el navegador a la cuenta del usuario (sin sesión/credenciales, red restringida).

## ✅ Hecho recientemente
- Intro corregida (superficie verde + grieta pequeña) en frames, clips y SB pages (los 12 planos de SEC 1).
- Prompts acortados a la mitad; prefijo `Make a … sheet of` dentro del campo visible.
- Versión **MINI** creada para locaciones (21) y diseños (48), con prefijo y `Studio Ghibli style`.
- Intro dividida en 2 placas: `@ErdiaSuperficieViva` y `@CorazonMuerto`.
- Todo en `main`.

## ⏭️ Próximos pasos posibles
1. Usuario genera las **69 hojas** en la app de Higgsfield (nano banana, ilimitado). *(en curso)*
2. Luego generar los **619 frames** adjuntando hojas de referencia.
3. Activar **GitHub Pages** para el link público.
4. Opcional: title cards / rótulos de año / lámina maestra de estilo.
5. Opcional: versión MINI también para los frames del storyboard (hoy son largos).

---
*Fin del documento de traspaso. Para retomar: lee esto, luego mira `STELLA_FUGAZ.html` o las pestañas MINI.*
