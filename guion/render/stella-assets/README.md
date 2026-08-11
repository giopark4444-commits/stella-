# STELLA FUGAZ · "El Nodo de Erdia" (Película 1) — ASSETS VISUALES

Carpeta de referencia visual de la peli. Todo generado con **GPT Image 2** (Studio Ghibli
style, 16:9, 2K), salvo 3 marcados *(nano)* hechos con **Nano Banana**.

## 📥 Cómo descargar las imágenes
El script `download_stella_assets.sh` baja TODO a `~/Desktop/stella assets/` ya organizado
y renombrado. En tu Mac/PC:
```bash
bash download_stella_assets.sh
```
*(Claude no pudo bajarlas él mismo: el CDN de Higgsfield está bloqueado en su entorno remoto
y no tiene acceso a tu Escritorio. Por eso el script lo corres tú.)*

## 📁 Estructura de carpetas
```
stella assets/
├── 01_locaciones/         19 fondos maestros (con su nº de ESC en el nombre)
├── 02_sublocaciones/      4 sub-áreas (Sala de la Fuente, Hangar, Poblado, Cielo)
├── 03_personajes/         25 (19 principales + 5 figurantes + gix apagado)
├── 04_naves/              5 naves/vehículos
├── 05_props/              7 props héroe
├── 06_keyframes_arranque/ 8 fotogramas clave (clips 1-8 del Arranque)
├── 07_keyframes_actos2-4/ 19 fotogramas clave (escenas 5-33)
└── 08_video/              CLIP 01 (prueba de video, 15s)
```
Convención de nombre: `tag_descripcion_ESCxx.png` → sabes qué es y a qué escena va.

---

## 🎬 DESGLOSE ESCENA POR ESCENA (33 escenas) vs LO GENERADO

> ✅ = generado · 🟡 = se cubre con un asset de otra escena (reutilizado) · ⬜ = pendiente (sobre la marcha)

### 起 KI — Erdia (Arranque)
| ESC | Título | Locación | Personajes/Props clave | Key frame |
|-----|--------|----------|------------------------|-----------|
| 1 | Tierra muerta / el brote | ✅ tierra_muerta | — | ✅ CLIP01 |
| 2 | Ciudad de Erdia + descenso | ✅ erdia_dorada | ✅ rio_luzagua, fuente_plaza | ✅ CLIP02-03 |
| 3 | Palacio · pasillos | ✅ palacio_pasillo | ✅ stella_14, gix, vera, selka_4, brazalete | ✅ CLIP05-06 |
| 4 | Taller de Naio | ✅ taller_naio | ✅ naio, orbe | ✅ CLIP07 |

### 承 SHŌ — Huida, nodriza, salto temporal
| ESC | Título | Locación | Personajes/Props | Key frame |
|-----|--------|----------|------------------|-----------|
| 5 | Sala de la Fuente (la caída) | ✅ taller_naio / ✅ SUB sala_fuente | ✅ naio, vera, selka_4, ✅ rey_humano, ⬜ g44 | ✅ ESC05 |
| 6 | Conductos / Hangar | ✅ conductos_hangar / ✅ SUB hangar | ✅ stella_14, gix, ✅ capsula_huida | ✅ CLIP08→ESC06 |
| 7 | Espacio · órbita de Erdia | ✅ espacio_orbita | ✅ capsula_huida, ✅ naves_rey | ✅ ESC06-07 |
| 8 | Celda de la nodriza | ✅ nave_nodriza | ✅ stella_14, ✅ gix_apagado, vosk, brog, nima | ✅ ESC08 |
| 9 | Puente de Theron | ✅ nodriza_puente | ✅ stella_14, theron | ✅ ESC09 |
| 10 | Planeta árido · combate | ✅ planeta_arido | ✅ marek, ✅ guerrera_misteriosa, ✅ g44 | ✅ ESC10 |
| 11 | Campo de batalla | ✅ planeta_batalla | ✅ stella_22, noah, orbe | ✅ ESC11 |
| 12 | Bodega / nido (cuadrilla) | ✅ nodriza_bodega | ✅ stella_22, brog, nima, noah, vosk | 🟡 (usa ESC16/bodega) |
| 13 | Planeta-bosque · cometas | ✅ planeta_bosque | ✅ stella_22, noah | ✅ ESC13 |
| 14 | Theron y la foto | ✅ nodriza_puente | ✅ theron, ✅ foto_familia | ✅ ESC14 |
| 15 | Montaje "lo que Theron ve" | ✅ palacio_podrido, sala_entrenamiento, refugio | ✅ naio_esclavo, selka_general, ✅ vera_mayor | 🟡 (usa ESC18/19) |
| 16 | Bodega (festejo) | ✅ nodriza_bodega | ✅ stella_22, brog, nima, noah | 🟡 |

### 転 TEN — Resistencia y regreso
| ESC | Título | Locación | Personajes/Props | Key frame |
|-----|--------|----------|------------------|-----------|
| 17 | Refugio subterráneo | ✅ refugio | ✅ vera_mayor, marek, ✅ korin, ✅ lessa | ✅ ESC17 |
| 18 | Palacio podrido · corredores | ✅ palacio_podrido | ✅ vera_mayor, marek, naio_esclavo | ✅ ESC18 |
| 19 | Sala de entrenamiento (la traición) | ✅ sala_entrenamiento | ✅ selka_general, marek, ✅ sable_selka | ✅ ESC19 |
| 20 | Puente de Theron | ✅ nodriza_puente | ✅ stella_22, theron | 🟡 (usa ESC09/14) |
| 21 | Nave pequeña · cabina (se tiñe) | ✅ nave_pequena_cabina | ✅ stella_adulta, noah, brog, nima, ✅ nave_pequena | ✅ ESC21 |
| 22 | Erdia podrida · poblado | ✅ erdia_podrida / ✅ SUB poblado | ✅ stella_adulta, noah, brog, nima | 🟡 |
| 23 | Preparativos (montaje) | ✅ erdia_podrida | ✅ stella_adulta, korin, lessa | 🟡 |
| 24 | Campos del palacio (la guerra) | ✅ erdia_podrida / ✅ SUB cielo | ✅ stella_adulta, orbe, g44 | ✅ ESC24 |

### 結 KETSU — El trono y la verdad
| ESC | Título | Locación | Personajes/Props | Key frame |
|-----|--------|----------|------------------|-----------|
| 25 | Sala del Trono · encuentro | ✅ sala_trono | ✅ stella_adulta, selka_general, orbe, sable_selka | ✅ ESC25-26 |
| 26 | El combate | ✅ sala_trono | ✅ stella_adulta, selka_general | ✅ ESC25-26 |
| 27 | La entrega (inversión de luz) | ✅ sala_trono | ✅ rey_humano, marek, selka_general, orbe | ✅ ESC27 |
| 28 | "Fui yo" · metamorfosis | ✅ sala_trono | ✅ rey_humano (metamorfosis), selka_general | ✅ ESC28 |
| 29 | Forma real | ✅ sala_trono | ✅ selka_general, ✅ vorthan_real | ✅ ESC29 |
| 30 | Renuncia + rescate | ✅ sala_trono | ✅ selka_manca, brog, nima, noah | 🟡 (usa ESC29/31) |
| 31 | Cielo · despegue de la nodriza | ✅ SUB cielo / espacio_orbita | ✅ theron, ✅ nave_pequena, ✅ nave_vorthan | ✅ ESC31 |
| 32 | Nave pequeña · bahía médica | ✅ nave_pequena_medica | ✅ stella_adulta(coma), selka_manca, ✅ tanque_soporte, brazalete | ✅ ESC32 |
| 33 | Interior muerto (cierre) | ✅ tierra_muerta | — (el brote, rima con ESC 1) | 🟡 (usa CLIP01) |

---

## 📊 INVENTARIO

| Categoría | Generado |
|-----------|----------|
| 🌍 Locaciones maestras | 19 |
| 🧩 Sub-locaciones | 4 |
| 👤 Personajes (19 ppal + 5 fig + gix apagado) | 25 |
| 🚀 Naves | 5 |
| 🔮 Props | 7 |
| 🎞️ Key frames (storyboard) | 27 |
| 🎥 Video | 1 clip |
| **TOTAL** | **~88 archivos** |

## ⬜ Pendiente (se hace sobre la marcha, no urgente)
- Figurantes de fondo restantes (pueblo dorado, tripulación, prisioneros, refugiados, multitudes…)
- Props de set-dressing (cuenco, maceta, mapas, consolas, cadenas…)
- VFX como ficha aislada (la mayoría ya viven dentro de los key frames)

## 📝 Notas de generación
- Quitar el token **"Miyazaki"** del prompt reduce rebotes del filtro.
- Formato que funciona: `Studio Ghibli style character sheet / background painting, 16:9`.
- **Nano Banana** como respaldo tras 2 fallos en GPT Image 2 (orbe, sable_selka, selka_manca).
