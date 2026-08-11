# ✅ CHECKLIST DE RENDER — STELLA FUGAZ

> Control de stills de referencia que se generan en Higgsfield (MCP).
> **Convención de nombre de cada imagen:** `TIPO_NN_tag_vN`
> - `TIPO` = `LOC` (locación) · `CHAR` (personaje) · `PROP` (prop héroe)
> - `tag` = el mismo tag de `BIBLIA_referencias.md` (sin `@`)
> - `vN` = variante (v1, v2, …)
> - Ejemplo: `LOC_01_erdia_dorada_v1`
>
> **Ajustes fijos:** Motor `gpt_image_2` (GPT Image 2 · OpenAI) · 16:9 · calidad high · 2k · estilo Studio Ghibli · location/character sheet.
> Estados: ⬜ pendiente · ⏳ enviada (generando) · 🟢 generada (sin aprobar) · ✅ aprobada (con `ref_id`)

---

## 🌍 LOCACIONES

### Arranque `[PILOTO]` — prioridad
> **Versión final:** rehechas con prompt corto `Studio Ghibli anime background painting, cinematic widescreen establishing shot, no characters. [1 frase]`. Estos job_ids son los buenos (se descartaron las versiones de prompt largo y las de Nano Banana).

| # | Archivo | Tag | Locación | Escenas | job_id (final) |
|---|---------|-----|----------|---------|----------------|
| 01 | `LOC_01_erdia_dorada` | `@erdia_dorada` | Erdia en su gloria | 2 | `51c330ad` |
| 02 | `LOC_02_palacio_pasillo` | `@palacio_pasillo` | Santuario Núcleo Profundo — pasillos | 3 | `414dba37` |
| 03 | `LOC_03_taller_naio` | `@taller_naio` | Taller de Naio (Sala de la Fuente) | 4,5 | `53c4e86f` |
| 04 | `LOC_04_tierra_muerta` | `@tierra_muerta` | Interior muerto del planeta | 1,2,33 | `6cc66ac9` |
| 05 | `LOC_05_erdia_podrida` | `@erdia_podrida` | Erdia 20 años después (árido-gris) | 22,23,24,31 | `50982707` |
| 06 | `LOC_06_sala_trono` | `@sala_trono` | La Sala del Trono (corrompida) | 25–30 | `7e004230` |
| 07 | `LOC_07_nave_nodriza` | `@nave_nodriza` | Nave nodriza del Cazador | 8 | `54199012` |
| 08 | `LOC_08_conductos_hangar` | `@conductos_hangar` | Conductos / Hangar del palacio | 6 | `a8854b53` |
| 09 | `LOC_09_espacio_orbita` | `@espacio_orbita` | Espacio · órbita de Erdia | 7 | `23984f0c` |
| 10 | `LOC_10_nodriza_puente` | `@nodriza_puente` | Nave nodriza · puente de Theron | 9,14,20 | `71882f51` |
| 11 | `LOC_11_nodriza_bodega` | `@nodriza_bodega` | Nave nodriza · bodega/nido | 12,16 | `37588edb` |
| 12 | `LOC_12_planeta_arido` | `@planeta_arido` | Planeta árido · ruinas | 10 | `57ef2fdc` |
| 13 | `LOC_13_planeta_batalla` | `@planeta_batalla` | Planeta · campo de batalla | 11 | `1162cdbd` |
| 14 | `LOC_14_planeta_bosque` | `@planeta_bosque` | Planeta-bosque · claro (noche) | 13 | `6e710200` |
| 15 | `LOC_15_refugio` | `@refugio` | Refugio subterráneo de la resistencia | 17 | `7662cc56` |
| 16 | `LOC_16_palacio_podrido` | `@palacio_podrido` | Palacio podrido · corredores (árido-gris) | 15,18 | `839488ae` |
| 17 | `LOC_17_sala_entrenamiento` | `@sala_entrenamiento` | Sala de entrenamiento (árido-gris) | 19 | `722ac588` |
| 18 | `LOC_18_nave_pequena_cabina` | `@nave_pequena_cabina` | Nave pequeña · cabina | 21 | `fb4fb043` |
| 19 | `LOC_19_nave_pequena_medica` | `@nave_pequena_medica` | Nave pequeña · bahía médica | 32 | `219a4978` |

### Sub-locaciones extra (áreas distintas dentro de una maestra · GPT Image 2)
| Sub | Maestra | Área | Escenas | ref_id |
|-----|---------|------|---------|--------|
| SUB_01 | `@taller_naio` | Sala de la Fuente | 5 | `032708e7` |
| SUB_02 | `@conductos_hangar` | Hangar | 6 | `718c17ce` |
| SUB_03 | `@erdia_podrida` | Poblado de la resistencia | 22,23 | `635f3ea3` |
| SUB_04 | `@erdia_podrida` | Cielo de Erdia | 31 | `411e1410` |

---

## 👤 PERSONAJES (character sheets)

### Arranque `[PILOTO]` — todas en 16:9, Ghibli acentuado
| # | Archivo | Tag | Personaje | Estado | ref_id (16:9) |
|---|---------|-----|-----------|--------|---------------|
| 01 | `CHAR_01_stella_14` | `@stella_14` | Stella (14 años) | 🟢 generada | `91f736eb` (prev) |
| 02 | `CHAR_02_gix` | `@gix` | Gix (ajolote de luz) | 🟢 generada | `6df90230` |
| 03 | `CHAR_03_vera` | `@vera` | Vera (madre) | 🟢 generada | `277e86db` |
| 04 | `CHAR_04_selka_4` | `@selka_4` | Selka (4 años, dormida) | 🟢 generada | `ed9c4bf8` (prev) |
| 05 | `CHAR_05_naio` | `@naio` | Naio (padre) | 🟢 generada | `cb71672a` |

### Más adelante `[futuro]` — todas en 16:9, Ghibli acentuado
| # | Archivo | Tag | Personaje | Estado | ref_id (16:9) |
|---|---------|-----|-----------|--------|---------------|
| 06 | `CHAR_06_selka_general` | `@selka_general` | Selka (la General) | 🟢 generada | `7bcc38fc` |
| 07 | `CHAR_07_stella_adulta` | `@stella_adulta` | Stella adulta | 🟢 generada | `13741e20` |
| 08 | `CHAR_08_theron` | `@theron` | Theron (el Cazador) | 🟢 generada | `b8b2b3fa` |
| 09 | `CHAR_09_brog` | `@brog` | Brog (tripulación) | 🟢 generada | `67ddd9dc` |
| 10 | `CHAR_10_nima` | `@nima` | Nima (tripulación) | 🟢 generada | `d5e105d9` |
| 11 | `CHAR_11_noah` | `@noah` | Noah (humano de la Tierra) | 🟢 generada | `a48d6010` |
| 12 | `CHAR_12_marek` | `@marek` | Marek (Rey infiltrado) | 🟢 generada | `6108f350` |
| 13 | `CHAR_13_vosk` | `@vosk` | Vosk (matón) | 🟢 generada | `48370937` |
| 14 | `CHAR_14_vorthan_real` | `@vorthan_real` | Vorthan / el Parásito | 🟢 generada | `90f40f08` |

---

## 🔮 PROPS HÉROE

### Arranque `[PILOTO]` — todos en 16:9
| # | Archivo | Tag | Prop | Estado | ref_id |
|---|---------|-----|------|--------|--------|
| 01 | `PROP_01_orbe` | `@orbe` | El Orbe / Fuente Madre | 🟢 generada | `d808886d` (nano) |
| 02 | `PROP_02_brazalete` | `@brazalete` | Brazalete de Stella | 🟢 generada | `b65e3b42` |
| 03 | `PROP_03_rio_luzagua` | `@rio_luzagua` | Ríos de luz-agua | 🟢 generada | `8271de35` |
| 04 | `PROP_04_fuente_plaza` | `@fuente_plaza` | Fuente de la plaza | 🟢 generada | `527b5ac8` |

### Más adelante `[futuro]`
| # | Archivo | Tag | Prop | Estado | ref_id |
|---|---------|-----|------|--------|--------|
| 05 | `PROP_05_sable_selka` | `@sable_selka` | Sable de luz de Selka | 🟢 generada | `800951ae` (nano) |

---

## 📊 Resumen
- **Locaciones:** 19/19 ✅ (todas en GPT Image 2, 16:9; `erdia_podrida` y `palacio_podrido` en versión árido-gris; `sala_entrenamiento` árido-gris a juego)
- **Personajes:** 14/14 ✅ (16:9, Ghibli acentuado; 12 en formato "single figure", stella_14 y selka_4 en versión previa por el filtro)
- **Props:** 5/5 ✅ (3 en GPT Image 2, orbe/sable en Nano Banana)
- **TOTAL stills:** 38/38 ✅

> **Nota técnica:** GPT Image 2 soltó muchos trabajos en silencio bajo carga; varios se relanzaron y los 2 props más rebeldes salieron por Nano Banana. Verificar siempre en `show_generations` antes de dar por hecho un job.
