# 📌 ESTADO Y CONTINUACIÓN — Stella Fugaz «El Nodo de Erdia»

> **Documento de traspaso.** Si me abres desde otra sesión/dispositivo, lee esto primero:
> resume el proyecto, el canon, qué está hecho, dónde vive cada cosa y qué falta.
> Última actualización: **2026-08-28** · Revisión de guion **v2.5**.

---

## 🎬 El proyecto
- **Película 1** de una saga (2-3 films). Tragedia animada, **21:9**. ⚠️ En los prompts el estilo se
  **describe, nunca se cita** (OpenAI bloquea nombres de estudio y de autor — ver `tools/estilo_canon.py`).
- **Duración objetivo:** ~48 min · **619 planos** (planos contemplativos, silencios, ritmo 間/ma).
- La saga se dividió en 3 partes por decisión **narrativa** (sola / sola / dúo), NO porque P1 fuera larga. P1 es lean.
- Logline: una niña huye de su mundo moribundo con la fuente de vida del planeta en la mano, con la promesa de volver, hacerse fuerte y salvar a la hermana que el enemigo le robó.

## 📖 CANON DEL GUION — v2.5 (2026-08-28) ⚠️ LEER ANTES DE USAR LOS PROMPTS

**Cambios v2.5 — APERTURA EN FRÍO (SEC 0):**
- La película **ya no empieza por el principio**. Arranca con ~90 segundos de acción pura: Stella
  adulta escalando el palacio en llamas bajo fuego, **sin diálogo, sin nombres, sin rótulo de año**.
  Corta en el instante en que rompe la cúpula de cristal y **cae**.
- **El corte de vuelta es de caída a caída:** ella se precipita al palacio, la cámara se precipita
  al planeta (SEC 1). El mismo movimiento dos veces: bajar al centro de algo y encontrarlo hueco.
- **La SEC 23 retoma ese plano** y esta vez no se corta.
- ⚠️ **La SEC 0 NO puede mostrar** la cara de Selka (solo silueta blanca), ni a Marek, ni a Vorthan,
  ni el interior del palacio. Ahí viven los tres secretos.
- **Motivo:** el proyecto compite contra cientos de otros; los primeros diez segundos deciden si
  alguien sigue viendo.
- **Duraciones fijadas (2026-08-28):** **SEC 0 = 2:00 · ~36 planos** (plaza 1:00 · fachada+cúspide 0:30 ·
  ducto+aterrizaje+silueta+golpe 0:30; en abierto, espectáculo, sin nombres, **muda entera**) y
  **SEC 23B = 2:00 · ~35 planos**, repartidos **plaza 1:00 · fachada 0:30 · cúspide 0:30** (en cerrado:
  los generales ya se vieron, la cámara se queda en las caras). Son el mismo suceso: **la 23B no
  repite, reencuadra.** Techo conjunto ~3:20 de 48 min.
- **La caída por el ducto es de la SEC 24, no de la 23B.** La 23B cierra en seco en *«Y se tira de
  cabeza»*; la 24 abre cayendo y revienta el techo de la sala del trono sin cortar. Son un solo
  movimiento y partirlos en dos escenas era un error de montaje.


**Cambios v2.6 — LA PLAZA REPLANTEADA (2026-08-28):**
- **El palacio es UNA ESFERA**, no una cúpula sobre un edificio: una bola de piedra del tamaño de una
  montaña apoyada sobre la ciudad. Hoja nueva `@PalacioEsfera`. La cúspide es su punto más alto.
- **Cuatro tipos de máquina imperial**, clonados por decenas, reconocibles **por la silueta**:
  `@RobotLinea` (infantería idéntica) · `@RobotPesado` (doble de alto, rompe formaciones) ·
  `@RobotCorredor` (bajo, cuatro patas, llega primero) · `@RobotDescarga` (patas larguísimas, no
  avanza nunca, dispara desde atrás — es el origen de las descargas de la fachada).
  ⚠️ **Ninguno es blanco:** metal oscuro casi negro; se ven porque el fuego se les refleja encima.
  `@RobotImperial` pasa a ser la hoja de familia: los cuatro juntos para leer las siluetas.
- **La película ABRE A RAS DE PISO**, no en negro ni desde el aire: dolly rasante entre escombros,
  cruzando pies de máquina y pies de los nuestros, con la guerra solo en el sonido. **Ese plano dura
  10 segundos exactos**: al segundo 10 la cámara ya está abierta en **plano medio** sobre los
  personajes, y no vuelve al suelo hasta que el disparo la tira.
- **La SEC 0 se genera en CUATRO prompts de 30 s clavados** (la plaza se lleva los dos primeros):
  `0:00–0:30` el suelo y el avance · `0:30–1:00` dentro de la carga · `1:00–1:30` el grito, el pasillo,
  la subida y la cúspide · `1:30–2:00` el ducto, el aterrizaje, la silueta y el golpe.
- **La plaza es un CONTRAATAQUE**, no una defensa: la resistencia AVANZA hacia la esfera y gana
  terreno. Cambió el verbo de toda la secuencia — de «aguantar» a «empujar».
- **TODO EL ASALTO EXISTE PARA MOVER A STELLA.** No atacan el palacio: le abren camino. Cada golpe de
  cada personaje gana un metro para ella. Ellos no van a entrar; ella sí. De ahí que ella no pelee en
  toda la plaza, y que su grito del 1:00 **no pida paso sino que cambie el destino** (no por la puerta,
  por arriba).
- **MÉTODOS DE CÁMARA — solo cuatro:** `dolly` · `steadycam` · `brazo mecánico` · `POV de dron`, y los
  planos lo más largos posibles. ⚠️ **Nunca cámara en mano**, nunca temblor de operador.
- **Erdia destruido pero BONITO dentro de su caos:** el cielo del año 24 tiene estrellas nítidas y el
  humo las atraviesa. Belleza y desastre en el mismo cuadro.
- **EL CONTRAPICADO (0:16–0:20):** único plano de la plaza donde solo hay dos cosas en cuadro, **ella y
  el cielo**. Es donde aparecen las naves por primera vez y donde se ve la belleza del planeta muerto.
- **Naves desde el primer segundo, pero LEJOS:** siluetas pequeñas cruzando muy arriba contra el cielo
  violeta. De cerca no se ve ninguna hasta **1:09**, cuando una pasa por debajo de las botas de Stella
  en plena subida. Lo que sí se ve desde el suelo son sus impactos caminando por la tierra.
- **La tripulación entra PRONTO:** al segundo 4 ya nos cruzamos con ellos por los pies, y Brogu tiene su
  primera acción **a los 10 segundos**, todavía dentro del plano rasante. Roster de la plaza y **cada uno
  pelea distinto, ninguno duplica a otro**: `@Brogu` abre camino · `@Nima` artefactos · `@MujerVerde`
  sube y tumba a los de descarga · `@HombrePulpo` atrapa en el aire con tres brazos · `@TrioHumano`
  (Noah entre ellos) aguanta flancos en formación · `@Vosk` trepa y tumba desde dentro · `@Gara` carga.
- ⚠️ `@MujerVerde` y `@HombrePulpo` llevan **nombre provisional** — falta que Gio los bautice.
  `@TrioHumano` = los tres humanos de la tripulación, Noah incluido (los demás secundarios son
  «clearly not human» en sus hojas).
- **La plaza va en PLANOS SECUENCIA con cámara-dron**, no en cortes: la cámara vuela, se engancha a un
  personaje, lo suelta, se va con otro, sube, gira y cae. Velocidad alta, todo en movimiento.
  Tres planos secuencia cubren el minuto (el choque · dentro · la decisión).
- **Regla de montaje nueva:** la cámara **no para en todo el minuto** hasta que cae al suelo con Enko.
  Esa quietud es el primer plano estático de la película y por eso pesa el doble. La segunda vez que
  se para es en la sala del trono.

**Cambios v2.4 — dos personajes rediseñados:**
- **Brog → `@Brogu`.** Ya **NO** es un gigante de piedra: es un ser con **aspecto de gorila**
  (pelaje oscuro, hombros de armario, brazos larguísimos, ojos pequeños y calmos). Sigue siendo
  lento, callado, el último de su especie, y sigue enseñándole a Stella su idioma muerto.
  ⚠️ Nada de roca, grietas ni luz interior en ningún prompt.
- **`@Nima` deja de tener cuatro brazos.** Es una **elfa de piel azulada y baja estatura**, y
  **la científica de la nave** (ya no «mecánica»). Su taller pasa a ser **laboratorio**.
  ⚠️ **Dos brazos.** Trabaja sobre un cajón para alcanzar la mesa y no lo menciona nunca.
- **Consecuencia de altura (SEC 27):** una elfa baja no puede cargar a una adulta con armadura →
  ahora **Vosk levanta a Selka**, Brogu carga a Stella y Nima va delante abriendo paso.
- Donde Nima abría paredes a la fuerza, ahora usa artefactos.

La fuente de verdad es `guion/GUION_P1_v2.md` (+ `ESCALETA_P1_v2.md`, sincronizada). **32 secuencias.**

**Cambios v2.3:**
- **SEC 12A NUEVA — Selka a los 9.** Pelea contra un autómata de combate entero y pierde porque
  **titubea**. Vorthan, avergonzado, le cruza el ojo izquierdo (única vez que se le rompe la cara).
  Ella se levanta y **destroza al autómata sin titubear**, y sigue golpeando chatarra mucho después
  de que dejó de moverse. **Es el segundo exacto en que se fabrica a la General.**
- **La cicatriz tiene origen** y se cobra en la SEC 26.
- **Fuera la nana** de todo el guion: en SEC 20A el remate es el pelo blanco de la muerta; en SEC 26,
  encajar quién era («la del piso, la de mi cuarto»).
- **Selka es CADETE en el año 14**, no General (15 años, aposentos en el palacio, criada por el Rey).
- **El muelle (SEC 26):** Vorthan sostuvo la resistencia 24 años para dejarle a Stella dónde atracar.
- Hojas nuevas: `@Selka9`, `@Selka9Herida`, `@SalaInstruccion`, `@AutomataInstruccion`.

**Cambios v2.2:**
- **Naio es PRISIONERO DEL PALACIO** (celdas del nivel de servicio) los 24 años — **nunca estuvo en las minas**.
  Vorthan lo conserva porque él encriptó el Orbe y es el único que podría saber cómo extraerlo.
- **La noche del año 14 ocurre entera dentro del palacio:** Marek le abre a Vera una reja de servicio;
  Vera ve a Naio en las celdas y sube por Selka.
- **La SEC 20 va en dos tiempos:** el público ve "a Selka" matar a Vera (es Vorthan con su cara; cierra
  con una sonrisa que solo se entiende en el segundo visionado); en la **SEC 20A** la Selka real descubre
  el arma en su propia mano, sin memoria. *(La nana se eliminó en v2.3.)*
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
- **Selka:** cicatriz sobre el ojo izquierdo **desde los 9 años** (se la hace Vorthan, SEC 12A);
  desde la SEC 27, **manca**.

## 📁 Dónde vive cada cosa (`guion/*.md`)
| Contenido | Archivo(s) | ¿Al día con v2.3? |
|---|---|---|
| **Guion canónico** | `GUION_P1_v2.md` (34 secuencias) | ✅ |
| **Guion técnico SEC 0** | `GUION_TECNICO_SEC0.md` — 45 planos, cámaras, refs y riesgos | ✅ |
| **Híbrido ES/EN** | `GUION_P1_v2_DIALOGOS_EN.md` | ✅ `tools/genhibrido.py` |
| **Escaleta** | `ESCALETA_P1_v2.md` | ✅ |
| **PDF** | `guion/render/GUION_P1_v2.pdf` (47 pág.) | ✅ `tools/guion_pdf.py` |
| Personajes (32) | `PROMPTS_PERSONAJES(_MINI).md` | ✅ |
| Locaciones (25) | `PROMPTS_LOCACIONES(_MINI).md` | ✅ |
| Naves y props | `PROMPTS_DISENOS(_MINI).md` | ✅ |
| Guion inglés / híbrido | `SCRIPT_P1_v2_EN.md`, `GUION_P1_v2_DIALOGOS_EN.md` | ❌ v2.0 — retraducir |
| Storyboard frames (619) | `PROMPTS_IMG_ACTO1/2/3.md` | ❌ largos y con canon viejo |
| Clips Seedance (233) | `PROMPTS_SB_ACTO1/2/3.md`, `PROMPTS_ACTO1/2/3.md` | ❌ ídem |
| Variante SEEDANCE (44) | `*_SEEDANCE.*` | ⚙️ `tools/seedance_safe.py --apply` |
| Material base histórico | `PELI1_v2_material_base.md` | 📜 histórico — el guion manda |

**Formato de los prompts (v2.3):** las versiones MINI son de **puro concepto** — una pregunta, cuatro
ejemplos, cero características, sin aspect ratio. Cola de estilo común, cambiable de golpe en los 81
con `tools/cola_estilo.py --set "..."`.

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
1. **Gio:** generar las hojas en la app de Higgsfield con los prompts MINI (nano banana). Las de
   personaje, locación y props **ya están al día**; los prompts de los *planos* no.
2. **Regenerar el corpus de planos** (frames y clips) de las secuencias tocadas por v2.2/v2.3 —
   y pasarlos al formato concepto. Es el grueso que queda.
3. **Retraducir** el guion inglés y el híbrido desde v2.3.
4. Hojas nuevas por generar: `@Selka9`, `@Selka9Herida`, `@SalaInstruccion`, `@AutomataInstruccion`,
   `@SelkaGeneralManca`, `@SalaTronoAbierta`, `@CieloAño24`, `@EnfermeriaNodriza`, `@CeldasPalacio`,
   `@PuñalSelka`, `@TransmisorVera`, `@NaveStellaRota`, `@CadenasEsclavo`.
5. **Decisión abierta:** vestuario de Selka en SEC 20 y 20A (propuesta: de gala la falsa, descalza
   la real — ver conversación).

---
*Para retomar: lee esto, luego `guion/GUION_P1_v2.md` (v2.5) y la escaleta. El guion manda sobre
cualquier prompt viejo.*
