# 🚀 RETOMAR AQUÍ — STELLA · *a falling star*

> **Estado al cerrar la sesión del 2026-08-30 · guion v2.8 · commit `bbb6b41`**
> Este documento es el punto de entrada. **No hace falta leer nada más para arrancar producción.**

---

## 0 · En una línea

El guion está **terminado y verificado** (40 secuencias, v2.8). La biblioteca de referencias de Gio
está **completa** (155 piezas). **Empieza la generación de imagen y clip.** Lo único pendiente de
verdad es que **las hojas de producción todavía describen una versión anterior de la película.**

---

## 1 · Por dónde se empieza

Hay **dos entregables**, generados desde la misma fuente, y sirven para cosas distintas:

| Archivo | Para qué | Artefacto |
|---|---|---|
| `guion/GUION_REFERENCIAS_v2.8.md` | **Promptear.** Cada nombre viene sustituido por su `@tag` | https://claude.ai/code/artifact/8a3073ba-81d0-47c0-88fb-b808f67c12c9 |
| `guion/GUION_CLASICO_v2.8.md` | **Leer.** Nombres normales | https://claude.ai/code/artifact/a4e1634c-ba6d-434c-a58e-1c43acf505e1 |

En el de referencias, cada `## SEC` abre con tres líneas 🏷️ — **locación · reparto · props**— antes
de la primera palabra de acción. Y **el tag cambia según la secuencia**: Stella tiene once estados,
Vera ocho, Selka nueve. Nunca uses un tag de Stella sin mirar en qué secuencia estás.

✅ **Verificado el 2026-08-30: cero referencias rotas.** Todo lo que el guion cita existe en los
paneles de Gio.

**La fuente de verdad para editar es `guion/GUION_P1_v2.md`.** Los dos entregables se regeneran
desde ahí; editarlos a mano no sirve de nada.

---

## 2 · ⚠️ Las cinco trampas de este repo

**① GitHub Pages NO publica desde `main`.** Publica desde la rama
`claude/erdia-node-script-review-fc983t`. **Todo push va a las dos ramas**, siempre:

```bash
git push origin main
git push origin main:claude/erdia-node-script-review-fc983t
```

**② La página viva se verifica en `/stella-/STELLA_FUGAZ.html`, NO en la raíz.**
La raíz es una portada de ~12 KB y **siempre da 0** al buscar cualquier cosa del guion.
👉 https://giopark4444-commits.github.io/stella-/STELLA_FUGAZ.html

**③ La cadena de generadores tiene orden estricto.** Saltarse uno deja archivos desincronizados:

```bash
python3 tools/genweb_guion.py   --apply   # guion → HTML + STELLA_FUGAZ.html
python3 tools/genhibrido.py     --apply   # versión con diálogos en inglés
python3 tools/seedance_safe.py  --apply   # limpia el corpus para Seedance
python3 tools/estilo_canon.py   --check   # que no se cuele ningún nombre de estudio
python3 tools/gentags.py                  # versión etiquetada con @tags
python3 tools/genentregables.py           # los dos entregables versionados
python3 tools/guion_pdf.py                # PDF
```

**④ `genhibrido.py` FALLA A PROPÓSITO.** Si añades un diálogo nuevo en español y no le pones su
entrada en `tools/dialogos_en.json`, el generador se para y **te lista las líneas que faltan**.
Eso no es un error: es la compuerta. Copia la lista, traduce, y vuelve a correrlo.

**⑤ El número de versión vive en cuatro sitios.** Al subir de versión hay que tocarlos todos:
`tools/genweb_guion.py` · `tools/genhibrido.py` · `tools/guion_pdf.py` · `tools/gentags.py`
y la cabecera de `guion/GUION_P1_v2.md`. `genentregables.py` lee la versión de la cabecera y la
estampa en el nombre de los archivos, así que si la cabecera está mal, todo sale mal.

---

## 3 · El canon que rompe prompts

Diez reglas. Cada una ha roto algo al menos una vez.

1. **Los dos relojes: dilatación 1:4.** Stella vive **5 años**, en Erdia pasan **20**. Se va con 14 y
   vuelve con 19. Selka tiene 21 y **es mayor que ella.** ⚠️ Era 24 en versiones viejas — **20**.
2. **Las partículas.** El Orbe y Gix viven en la **palma izquierda**. Los **dos brazaletes** (uno por
   muñeca, sirve cualquiera) son el mando. Todo lo que sale o entra **viaja como partículas** y
   **pasa por la palma.** Nunca aparece de la nada.
3. **La esfera solo se materializa cuatro veces** en toda la película. El resto del tiempo está dentro.
4. **Los brazaletes son siempre los mismos** y **cambian de aspecto una sola vez** — SEC 20D, cuando
   Theron le da el último traje.
5. **Las armas se reparten por sangre.** El que tiene poder no lleva nada; **el que no tiene poder
   lleva acero.** Noah espada · Carl lanza · Lucy arco · rebeldes de pelo oscuro. ⚠️ **No hay pistolas,
   rifles, balas ni gatillos** en ningún plano — hojas y astas sí.
6. **Theron NO puede rastrear a Vortham.** Su poder exige **haberlo visto de verdad, una vez**, y en
   veinte mil años **no le ha visto la cara a ningún Parásito.** En la SEC 27 lo tiene a doscientos
   metros y le acierta, pero **a contraluz: una forma, no una cara.** ⚠️ Ningún prompt de la SEC 27
   puede mostrarle el rostro desde el punto de vista de Theron.
7. **El único rastro que existe al final es Stella.** Al abrir la mano se le fueron sus partículas
   dentro del Orbe. La brasa de Gix en su pecho **es a la vez su vida y la señal.**
8. **El Orbe está encriptado en la familia, no en Stella.** Vortham puede tenerlo en la mano y no
   puede usarlo. Por eso crió a Selka: **no para tener una General, para tener una MANO.**
9. **Toda hoja de locación va en VISTA PANORÁMICA.** Un plano cerrado no deja entender el planeta.
   La receta está en la sección 8.
10. **Nunca texto dentro de la imagen. Nunca color quemado.**

Más detalle en `guion/CONTINUIDAD.md` — ahí está el estado de cada cosa secuencia por secuencia,
para poder rodar en desorden.

---

## 4 · Qué se decidió en esta sesión (v2.7 → v2.8)

**El final se cierra con un recuerdo de Theron.** En la SEC 20C —el lago del puerto estelar— Stella
le propone **entregar el Orbe a propósito**, que parezca que se lo quitaron, y seguir la nave hasta
el planeta de los Parásitos. Theron le dice que no, y se va soltándole una condición sin darse
cuenta: *«si algún día le abres la mano a esa cosa, que no sea por mí.»* En la SEC 24 ella la
cumple —la abre **por su hermana**— y él no lo va a saber nunca.

**Corrección de canon de Gio:** Theron nunca ha visto a Vortham ni a un Parásito en su forma real,
así que **no puede localizarlo.** El guion se contradecía en cuatro sitios; los cuatro corregidos.
Consecuencia: la idea del recuerdo deja de ser un adorno y pasa a ser **estructuralmente obligatoria**
— sin el pedazo de Stella dentro del Orbe, esta gente no tiene adónde ir y no hay Película 2.

**Nima cierra el mecanismo** en la SEC 29B: *«No es una señal. Es ella.»* Y remata: *«Si se muere, lo
perdemos.»* Eso convierte mantener viva a Stella en la misión de la P2, no en un sentimiento.

**Rótulo final corregido:** ya no dice *EL NODO DE ERDIA*.

---

## 5 · ⚠️ Decisiones ABIERTAS — no cerrarlas por tu cuenta

Gio las quiere decidir **con la película montada, no en la página.**

**① El final está bifurcado (SEC 29B).** A la pregunta de Nima —*«¿Entonces lo hizo.»*— hay **dos
réplicas escritas** dentro del guion, marcadas con un bloque enmarcado:

| | Réplica | Qué significa |
|---|---|---|
| **A** | *«No lo sé.»* | El plan existió, pero abrió la mano por su hermana. El público sabe la verdad; la sala no |
| **B** | *«Lo hizo.»* | El plan era real. Termina en jugada, no en derrota |

👉 **Rodar las dos.** Es una línea y su remate: mismo plano, misma luz, mismo día.
👉 **Ningún otro clip de la película puede dar por buena ninguna de las dos** — ni un plano, ni una
mirada, ni una línea en otra escena.

**② El proyector de Vera y el mapa del salón.** Gio dijo: *«esas escenas no me convencen mucho»* y
después *«olvídate del mapa, lo del proyector lo decidimos luego cuando lleguemos ahí, de momento
déjalo.»*
👉 **No tocar nada.** Las escenas se quedan como están hasta que él llegue a ellas.
👉 El diagnóstico, por si sirve entonces: el **bloque 6 del montaje dice lo mismo dos veces** (el
mapa donde Erdia no se enciende, y el proyector que no enciende), y la escena siguiente —el lago—
lo dice una tercera vez. La propuesta que quedó sobre la mesa era que **el mensaje de la madre se
proyecte en la carta estelar** en vez de en un aparato de mesa, lo cual mata el prop y cumple una
frase que el guion ya pide: *«llenando la habitación más grande de la nave.»*

---

## 6 · Qué falta

### Arte — prácticamente nada
De **33 piezas** iniciales quedan **2**, y las dos están congeladas dentro de la decisión ⑤②:
el **mapa del salón** y el **proyector de Vera**. Todo lo demás existe.

Se cerró en esta sesión: los tres pilotos (`@pilot-1` · `@pilot-2` · `@char_pilot-3`), Stella en el
tanque (`@char_stella-recovery-tank`), los 11 mundos del montaje, los cristales de Nima y las armas
de los humanos (**los dos están en skills**, no en props).

### El corpus de producción — esto sí es grande
- **`guion/GUION_TECNICO.csv`** tiene desglose de planos para **29 secuencias de 40**. Faltan **12**:
  la **SEC 0** y las once con letra — **10A · 12A · 13B · 15B · 20A · 20B · 20C · 20D · 23B · 29A · 29B**
  (el mercado, el tinte, el montaje, el puerto estelar y el final entero).
- **Y las 29 que existen describen la película vieja:** `SEC 8 — híper-salto` (ya no lo hace Stella),
  `SEC 9 — Balcón real` (se rueda desde la plaza, de noche), `SEC 18 — Camarote` (se rueda en el
  salón), `SEC 19/20 — Año 14` (ese año ya no existe), `SEC 29 — Enfermería` (ahora son 29A y 29B).
- **76 archivos dentro de `guion/` todavía dicen «El Nodo de Erdia».**

🚫 **NO PROMPTEAR DESDE `guion/PROMPTS_*`.** Ese corpus —619 frames de storyboard y 233 clips—
describe la película anterior. **La única fuente buena es `GUION_REFERENCIAS_v2.8.md`.**

**Consecuencia práctica: todavía no hay duración total de la película.** Sale del desglose, y el
desglose está desincronizado.

### Pendiente de Gio
- **La lista de habilidades con sus referencias.** Ya dijo que los cristales de Nima y las armas de
  los humanos están ahí. Falta la lista completa para cruzarla contra el guion, igual que se hizo
  con personajes, locaciones y props.

---

## 7 · La biblioteca de Gio · 155 referencias

**47 locaciones · 87 personajes · 21 props.** Cruzadas contra el guion el 2026-08-30: **cero rotas.**

⚠️ **El nombrado es irregular y hay que respetarlo tal cual está.** Unas llevan prefijo y otras no
(`@planet-of-salt` vs `@loc_planet-of-rice`), y **hay erratas ya generadas que son ahora el nombre
correcto**: `@loc_modershipo-hospital` · `@planet-flating-waterfalls` ·
`@loc_erdia-palace-traingin-room` · `@loc_eridia-orbe-room` · `@loc_eridia-from-space` ·
`@ship-1-dust-Erdia` (con E mayúscula) · `@ship-4-enemyy` · `@robot-cyclop-s1s2`.
**Copiar el tag exacto. Una letra de más y la referencia no carga, y el generador no protesta.**

Los 11 mundos del montaje ya generados:
`@planet-of-salt` · `@loc_planet-of-rice` · `@loc_planet-of-permanent-shades` · `@planet-coral-reef` ·
`@planet-boreal-dunes` · `@planet-suspended-lakes` · `@planet-flating-waterfalls` ·
`@planet-of-permanent-eclipse` · `@planet-of-rings` · `@planet-of-comets-sky` · `@planet-of-comets`

---

## 8 · La receta de las locaciones panorámicas

Regla fija de Gio: **siempre vista panorámica.** Un plano cerrado no deja entender el planeta.
Este bloque va **al principio** de todo prompt de locación:

```
EXTREME WIDE PANORAMIC ESTABLISHING SHOT, ultra-wide cinematic aspect ratio.
Camera low, close to the ground, looking out across the landscape. Horizon sits
low — roughly the lower 40% of frame — so the sky dominates.
Three depth layers: something close to the lens, the main subject in the middle,
haze and a large celestial body at the far horizon.
The landscape must read as an entire world, not as a corner of one.
No close-ups, no detail crops. No text of any kind in the image.
```

Y cierra siempre con la línea de Gio, literal:

```
ghibli style and watercolor texture and watercolor technic
```

**Lo que hace que un mundo funcione:** cámara baja · horizonte al 40% · tres capas de profundidad ·
**un objeto celeste enorme** · **un elemento terrestre imposible** · bruma cálida en la distancia.
Y para mundos de cristal: el cristal tiene que estar **incrustado sobre algo orgánico** —roca,
árboles, agua— porque si todo es del mismo material el ojo pierde la escala.

---

## 9 · Comandos

```bash
cd ~/stella-

# cadena completa tras editar el guion
python3 tools/genweb_guion.py --apply && \
python3 tools/genhibrido.py --apply && \
python3 tools/seedance_safe.py --apply && \
python3 tools/estilo_canon.py --check && \
python3 tools/gentags.py && \
python3 tools/genentregables.py && \
python3 tools/guion_pdf.py

# comprobar que el guion sigue entero
grep -c "^## SEC" guion/GUION_P1_v2.md          # debe dar 40

# cruzar el guion contra la biblioteca (cero = todo resuelve)
grep -ohE '@[a-z][a-zA-Z0-9_-]*' guion/GUION_P1_v2_TAGS.md | sort -u

# publicar en las dos ramas
git push origin main && \
git push origin main:claude/erdia-node-script-review-fc983t

# verificar la página viva (NO la raíz)
curl -s https://giopark4444-commits.github.io/stella-/STELLA_FUGAZ.html | grep -c "v2.8"
```

---

*Cerrado el 2026-08-30 · guion v2.8 · 40 secuencias · commit `bbb6b41` en las dos ramas.*
