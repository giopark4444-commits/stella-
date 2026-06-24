# BIBLIA DE REFERENCIAS — STELLA FUGAZ (render Seedance / Higgsfield)

> **Qué es esto.** El "tablero" que conecta la historia con Higgsfield. Cada elemento
> recurrente (personaje, locación, prop) tiene un **tag** y un campo **`ref_id`**.
> Flujo de trabajo:
> 1. Generamos el *still de referencia* de cada elemento (con su prompt de abajo).
> 2. Lo apruebas → registramos el elemento en Higgsfield → pego su **`ref_id`** aquí.
> 3. En cada prompt de 15 s (ver `ARRANQUE_planos.md`) invocamos el tag → el render
>    usa siempre la misma cara, el mismo color, la misma forma. Eso mata la inconsistencia.
>
> **Cómo se rellena `ref_id`:** mientras esté en `—` el elemento aún no existe en Higgsfield.
> En cuanto generemos y aprobemos su still, queda con su identificador.

---

## ⚙️ AJUSTES GLOBALES (cambia aquí y cambia toda la peli)

**`@STYLE`** (look maestro — se concatena a todos los prompts):
```
hand-painted 2D anime background in the style of classic Studio Ghibli feature films
(Nausicaä, Princess Mononoke, Spirited Away), lush painterly watercolor-and-gouache
environments, soft naturalistic light, gentle gradients in the sky, rich but warm color
palette, hand-drawn organic detail, no harsh CGI, no 3D plastic render, cinematic
widescreen composition, Miyazaki / Kazuo Oga background-art sensibility
```
**Motor de imagen:** GPT Image 2 (definido con Gio). Locaciones SIN personajes (solo entorno).

**`@NEGATIVE`** (lo que NO queremos, en todos):
```
photorealistic live action, plastic CGI sheen, text, watermark, logo, extra fingers,
deformed hands, warped faces, flat lighting, modern Earth objects, cars, guns,
visible cables, low detail, blurry, jpeg artifacts
```

**Regla de mundo (no romper nunca):** los *naieli* tienen el **pelo blanco puro** (es un voto,
no un rasgo de raza). Toda la luz es **luz-agua** (nai): fluye, no se posee. Nada de tecnología
"de la Tierra" en Erdia. Hora dorada en el Arranque.

---

## 1. PERSONAJES

> `[PILOTO]` = aparece en el Arranque (primeros 8 clips). Esos los generamos primero.

### `@stella_14` · Stella (14 años) `[PILOTO]`
- **ref_id:** —
- **Quién:** protagonista. Adolescente despreocupada; nunca le ha pasado nada malo.
- **Prompt de referencia:**
```
Character reference sheet, full body and face close-up, a 14-year-old alien girl,
pure bright white long flowing hair, fair luminous skin, large expressive eyes that
catch light, light woven tunic of soft organic fabric in cream and pale gold, a glowing
light-water bracelet on her wrist, joyful carefree expression, neutral background. @STYLE
```

### `@gix` · Gix (ajolote de luz) `[PILOTO]`
- **ref_id:** —
- **Quién:** mascota bioluminiscente del brazalete; regalo del padre. Protege a Stella. Es nai puro.
- **Prompt de referencia:**
```
Creature reference, a bioluminescent axolotl made of living light-water, the size of a
house cat, translucent glowing body, luminous feathery gills like fronds of light,
undulating tail, releases small warm glowing bubbles, swims through the air, soft cyan
and warm gold glow, neutral dark background. @STYLE
```

### `@vera` · Vera (madre, 40s) `[PILOTO]`
- **ref_id:** —
- **Quién:** madre de Stella y Selka. Belleza cansada y verdadera. Luego, líder de la resistencia.
- **Prompt de referencia:**
```
Character reference, a beautiful alien woman in her forties, impeccable pure white hair
worn up, weary but warm and dignified face, fine lines that read as truth not age, elegant
flowing robe in deep teal and silver, calm protective presence, neutral background. @STYLE
```

### `@selka_4` · Selka (hermanita, 4 años, dormida) `[PILOTO]`
- **ref_id:** —
- **Quién:** la hermana pequeña. En el Arranque está dormida en brazos de Vera.
- **Prompt de referencia:**
```
Character reference, a sleeping 4-year-old alien girl, soft pure white hair, round
peaceful face, cheek pressed against a shoulder, tiny pale tunic, serene, neutral
background. @STYLE
```

### `@naio` · Naio (padre, 50s) `[PILOTO]`
- **ref_id:** —
- **Quién:** Científico Jefe, Guardián de la Fuente. Brillante y distraído; ternura grave.
- **Prompt de referencia:**
```
Character reference, an alien man in his fifties, white hair with faint silver, kind
distracted eyes of a brilliant scientist who forgets to eat, layered scholar's robe in
warm grey and amber with luminous instrument-thread details, gentle authority, neutral
background. @STYLE
```

### `@selka_general` · Selka (la General, adulta) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, an adult alien woman, perfect impossibly white hair (artificially
maintained), cold flawless beautiful face, scarred discipline in her eyes, dark armored
uniform of the Hollow Guard with pale light accents, a thin light-blade at her side,
imperial and hollow, neutral background. @STYLE
```

### `@stella_adulta` · Stella adulta (pelo teñido) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, the same girl now a young woman, hair dyed dark to hide her white
naieli roots (pale roots showing), hardened determined eyes, worn spacefarer's jacket and
gear of a hunter's crew, the glowing light-water bracelet still on her wrist, neutral
background. @STYLE
```

### `@theron` · Theron (el Cazador) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, a tall alien hunter, dry neutral unreadable expression (not warm),
weathered face, utilitarian dark coat and tracking gear, an eye/sensor device that lets
him locate anyone, cold professional presence, neutral background. @STYLE
```

### `@brog` · Brog (tripulación, leal) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, a big burly good-hearted alien crew member, rough features, warm
loyal eyes, practical worn flight gear, gentle giant energy, neutral background. @STYLE
```

### `@nima` · Nima (tripulación) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, a quick agile alien crew member, sharp clever eyes, light practical
flight gear with tools, wry expression, neutral background. @STYLE
```

### `@noah` · Noah (guerrero humano de la Tierra) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, a human young man from Earth (clearly NOT a white-haired naieli),
dark hair, ordinary human features, scavenged warrior's armor, grounded and out of place
among aliens, brave tired eyes, neutral background. @STYLE
```

### `@marek` · Marek (2º líder de la resistencia = el Rey infiltrado) `[futuro]`
- **ref_id:** —
- **Quién:** se ve como camarada noble y de fiar; ES el Rey/Vorthan disfrazado (el topo). Diseño cálido y confiable.
- **Prompt de referencia:**
```
Character reference, a warm trustworthy alien man, white hair, open honest comrade's
face, scarred resistance-fighter clothing, the kind of friend everyone trusts — with the
faintest uncanny stillness behind the eyes (he is the disguised King), neutral
background. @STYLE
```

### `@vosk` · Vosk (el matón de la nave nodriza) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Character reference, a hard aggressive alien crew bully, harsh angular features, sneering
expression, heavy worn gear, intimidating build, neutral background. @STYLE
```

### `@vorthan_real` · Vorthan / el Parásito (forma real) `[futuro]`
- **ref_id:** —
- **Prompt de referencia:**
```
Creature reference, the Parasite's true form, a colossal shapeshifting hive-mind entity,
shifting faces of those it devoured rippling across its surface, devouring darkness that
swallows light instead of channeling it, terrifying anti-light silhouette, neutral
background. @STYLE
```

---

## 2. LOCACIONES

### `@tierra_muerta` · El interior muerto del planeta `[PILOTO]`
- **ref_id:** —
```
Environment reference, extreme close detail of dead biomechanical soil, black metallic
veined crust, long dead, drained of life; in the exact center a single trembling green
sprout pushing through. Macro, intimate, ominous silence. @STYLE
```

### `@erdia_dorada` · Ciudad de Erdia en su gloria `[PILOTO]`
- **ref_id:** —
```
Environment reference, a utopian alien city that was grown not built, towering organic
crystal spires curving upward like giant reeds, thin suspended rivers of glowing
light-water flowing through the air with no cables, bridges of light, people walking,
impossibly clean deep blue sky, golden hour, peaceful, breathtaking. @STYLE
```

### `@palacio_pasillo` · Palacio — pasillos de mármol `[PILOTO]`
- **ref_id:** —
```
Environment reference, a grand imperial palace corridor of warm white marble, tall arched
windows pouring golden light, faint living light-water details in the walls, serene and
luminous. @STYLE
```

### `@taller_naio` · Palacio — Taller de Naio `[PILOTO]`
- **ref_id:** —
```
Environment reference, a tall luminous laboratory full of half-living instruments that
breathe light and tilt as you pass, floating holographic projections; at the far end,
behind a translucent containment field, a head-sized sphere of glowing light-water tints
every surface blue. @STYLE
```

### `@sala_trono` · La Sala del Trono `[futuro]`
- **ref_id:** —
```
Environment reference, a vast cold throne hall, once sacred now corrupted, the channel of
light gone dark and stagnant, oppressive grandeur, sickly inverted light. @STYLE
```

### `@nave_nodriza` · La nave nodriza del Cazador `[futuro]`
- **ref_id:** —
```
Environment reference, the interior of a vast hunter mothership, industrial and lived-in,
cold metal corridors, viewports onto fields of stars, utilitarian alien crew quarters.
@STYLE
```

### `@erdia_podrida` · Erdia 20 años después (podrida) `[futuro]`
- **ref_id:** —
```
Environment reference, the same grown city now choking, toxic grey mist, the suspended
light-water rivers run dark and stagnant, white-haired people stained grey with soot,
old war-robots overgrown then re-armed, dystopia as desecration of a once-holy place.
@STYLE
```

---

## 3. PROPS HÉROE

### `@orbe` · El Orbe / la Fuente Madre `[PILOTO]`
- **ref_id:** —
```
Prop reference, the Mother Source: a head-sized sphere of living light-water, slowly
pulsing like a sleeping heart, held behind a translucent containment field, casting
rippling blue light on everything around it, sacred and alive. @STYLE
```

### `@brazalete` · El brazalete de Stella `[PILOTO]`
- **ref_id:** —
```
Prop reference, an elegant wrist bracelet of woven light, emitting a thread of
light-water that can take living shape, warm soft glow, a mother's gift. @STYLE
```

### `@rio_luzagua` · Los ríos de luz-agua `[PILOTO]`
- **ref_id:** —
```
Prop reference, thin rivers of glowing light-water suspended in mid-air with no support,
flowing slowly, people brush them with their fingertips as they pass, warm and sacred.
@STYLE
```

### `@fuente_plaza` · La fuente de la plaza `[PILOTO]`
- **ref_id:** —
```
Prop reference, a small public fountain of liquid light, an old caretaker dips a bowl and
lifts it full of glowing liquid light, children gather to listen to it. @STYLE
```

### `@sable_selka` · El sable de luz de Selka `[futuro]`
- **ref_id:** —
```
Prop reference, a thin elegant light-blade of the Hollow Guard's General, cold pale
cutting light. @STYLE
```

---

> **Siguiente paso:** generar los stills `[PILOTO]` (5 personajes + 4 locaciones + 4 props),
> aprobarlos uno por uno, y pegar sus `ref_id`. Con eso, el `ARRANQUE_planos.md` queda listo
> para renderizar los 8 clips con consistencia total.
