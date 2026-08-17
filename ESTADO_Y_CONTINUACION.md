# 📌 ESTADO Y CONTINUACIÓN — Stella Fugaz «El Nodo de Erdia»

> **Documento de traspaso.** Si me abres desde otra sesión/dispositivo, lee esto primero:
> resume el proyecto, el canon, qué está hecho, dónde vive cada cosa y qué falta.
> Última actualización: **2026-08-17** · Revisión de guion **v2.2**.

---

## 🎬 El proyecto
- **Película 1** de una saga (2-3 films). Tragedia animada, estilo **Studio Ghibli + Satoshi Kon**, **21:9**.
- **Duración objetivo:** ~48 min · **619 planos** (découpage Ghibli/Kon con planos contemplativos, silencios, ritmo 間/ma).
- La saga se dividió en 3 partes por decisión **narrativa** (sola / sola / dúo), NO porque P1 fuera larga. P1 es lean.
- Logline: una niña huye de su mundo moribundo con la fuente de vida del planeta en la mano, con la promesa de volver, hacerse fuerte y salvar a la hermana que el enemigo le robó.

## 📖 CANON DEL GUION — v2.2 (2026-08-17) ⚠️ LEER ANTES DE USAR LOS PROMPTS
La fuente de verdad es `guion/GUION_P1_v2.md` (+ `ESCALETA_P1_v2.md`, sincronizada). Cambios v2.2:
- **Naio es PRISIONERO DEL PALACIO** (celdas del nivel de servicio) los 24 años — **nunca estuvo en las minas**.
  Vorthan lo conserva porque él encriptó el Orbe y es el único que podría saber cómo extraerlo.
- **La noche del año 14 ocurre entera dentro del palacio:** Marek le abre a Vera una reja de servicio;
  Vera ve a Naio en las celdas y sube por Selka.
- **La SEC 20 va en dos tiempos:** el público ve "a Selka" matar a Vera (es Vorthan con su cara; cierra
  con una sonrisa que solo se entiende en el segundo visionado); en la **SEC 20A** la Selka real descubre
  el arma en su propia mano, sin memoria, y tararea la nana.
- **El acto 3 abre con la SEC 20B (el tinte y el permiso):** Theron concede la misión ("Bajas. Miras.
  Subes."), Nima le tiñe el pelo. Transición en pantalla de @StellaPeloCorto → @StellaTeñida.
- **Erdia avanza 24 años** (antes 20): Stella vuelve de **~20**, **Selka tiene 25**. Rótulo `AÑO 24`.
- **Los dos legados de Vera:** (1) la **señal lanzada al vacío** (SEC 12) — es lo que Theron le entrega a
  Stella en la SEC 18 (reemplaza a la "foto/proyector" antigua); (2) **"el palacio no tiene cimientos"**
  (SEC 19) — se lo confía a Naio, y en la SEC 29 Naio se lo ofrece a Theron: *"Yo sé por dónde se abre"*
  (el arma de la P2).
- **Marek rescató a Vera** de la sala del Orbe (por eso Vorthan la dejó tirada: la estaba reservando).
  La resistencia entera es una red suya. En la SEC 26 lo confiesa con crueldad total.
- **Clímax reordenado (SEC 27):** Vorthan ve la **brasa de Gix** (sabe que Stella no murió — le arruinó
  el placer); Selka se levanta **fría** y elige bando; la transformación en Parásito es una **rabieta**,
  no un truco.
- **Korin** le dice a Stella la verdad sobre Vera en la SEC 22 (tapaba un agujero: en la SEC 24 ella le
  reprocha a la General la muerte de la madre — antes nadie se lo había contado).
- **Vera sobrevive al ataque de S1G1** — la herida es "la atraviesa por la espalda" (ya NO "le perfora
  el corazón", incompatible con sobrevivir 3 días).
- **Theron:** su poder exige **referencia física**; nunca vio a Vorthan (por eso 20.000 años sin cazarlo)
  y **no sabe que es cambiaformas** (entró tras la transformación). En SEC 27 por fin lo VE → puede
  rastrearlo (motor de la P2).

## 🎨 Canon visual (IMPORTANTE — no equivocarse)
- **Intro:** superficie de Erdia **VERDE, sana y viva**, con **UNA grieta pequeña**; al bajar, el corazón
  muerto (`@CorazonMuerto`). La superficie NO es corteza rocosa.
- **Ojos:** Stella y Naio **ámbar**. Vera y Selka, **gris-azul**. Noah: pelo oscuro, ojos marrones.
  Korin, Lessa y pilotos NO son de pelo blanco (el pelo blanco es de la línea familiar).
- **Gix:** NO humano — axolote de luz (luzagua-azul con puntos dorados).
- **Naiel/naieli** = la especie/pueblo. **Luzagua** = agua-y-luz que brilla.
- **Selka:** cicatriz sobre el ojo izquierdo desde cadete; desde la SEC 27, **manca** (falta hoja).

## 📁 Dónde vive cada cosa (`guion/*.md`)
| Contenido | Archivo(s) | ¿Al día con v2.2? |
|---|---|---|
| **Guion canónico** | `GUION_P1_v2.md` | ✅ |
| **Escaleta** | `ESCALETA_P1_v2.md` | ✅ |
| Guion inglés / híbrido | `SCRIPT_P1_v2_EN.md`, `GUION_P1_v2_DIALOGOS_EN.md` | ❌ v2.0 — retraducir |
| Locaciones (21) | `PROMPTS_LOCACIONES(_MINI).md` | ❌ faltan @CeldasPalacio, enfermería, cielo año 24 |
| Personajes (31) | `PROMPTS_PERSONAJES.md` | ❌ edades (Selka 21→25), @NaioEsclavo→celdas |
| Naves+Props | `PROMPTS_DISENOS(_MINI).md` | ❌ faltan puñal de Selka, transmisor de Vera, nave rota |
| Storyboard frames (619) | `PROMPTS_IMG_ACTO1/2/3.md` | ❌ SEC 12/18/19/20/22/23/26/27/29 cambiaron |
| Clips Seedance (233) | `PROMPTS_SB_ACTO1/2/3.md`, `PROMPTS_ACTO1/2/3.md` | ❌ ídem |
| Variante SEEDANCE (42 archivos) | `*_SEEDANCE.*` | ⚙️ se regeneran con `tools/seedance_safe.py --apply` |
| Material base histórico | `PELI1_v2_material_base.md` | 📜 histórico — el guion manda |

## 🌐 La web (todo navegable con botón copiar)
- **Portada:** `index.html` · **App única:** `STELLA_FUGAZ.html` (~7.4 MB, todo embebido).
- **⚠️ GitHub Pages publica desde la rama `claude/erdia-node-script-review-fc983t`, NO desde `main`.**
  Publicar = `git push origin main && git push origin main:claude/erdia-node-script-review-fc983t`.
  Verificar SIEMPRE desde fuera con `curl` buscando una cadena nueva.
- **Generadores:** `tools/seedance_safe.py` (variante Seedance, con pruebas) y `tools/genweb_guion.py`
  (regenera `GUION_WEB.html` + variante + parchea la pestaña del guion en `STELLA_FUGAZ.html`).
  Los demás generadores históricos (locweb, designweb, imgframes, sbpages, onefile…) **siguen sin
  versionar** — recrearlos si hay que regenerar esas otras pestañas.

## ⏭️ Pendientes
1. **Gio:** generar las 69 hojas + 619 frames en la app de Higgsfield (nano banana; los prompts de las
   escenas cambiadas en v2.2 hay que regenerarlos ANTES de gastar créditos en esos planos).
2. **Regenerar el corpus de prompts** de las secuencias tocadas por v2.2 (lista arriba).
3. **Retraducir** el guion inglés y el híbrido desde v2.2.
4. Hojas nuevas: `@CeldasPalacio`, enfermería de la nodriza, cielo del año 24, puñal de Selka,
   transmisor de Vera, `@NaveStella` rota, Selka manca.

---
*Para retomar: lee esto, luego `guion/GUION_P1_v2.md` (v2.2) y la escaleta. El guion manda sobre
cualquier prompt viejo.*
