#!/bin/bash
# ============================================================
#  STELLA FUGAZ · "El Nodo de Erdia"
#  Crea en tu ESCRITORIO toda la estructura de carpetas para
#  archivar las referencias de la película.
#  v2: los nombres de personaje/nave/locación/prop llevan la @
#      tal cual el prompt, y hay una carpeta 09_STORYBOARDS.
#  → Doble clic para ejecutar (Mac). Si no abre: clic derecho →
#    Abrir. O en Terminal:  bash CREAR_estructura_Stella.command
# ============================================================
set -e
BASE="$HOME/Desktop/Stella_Fugaz_Referencias"
echo "Creando estructura en: $BASE"
mk() { mkdir -p "$BASE/$1"; }

PERS="@StellaRopa @StellaArmadura @StellaPeloCorto @StellaTeñida @VeraRopa @VeraArmadura @VeraEncapuchada @Naio @NaioEsclavo @NaioRescatado @SelkaBebe @SelkaCadete @SelkaGeneral @SelkaNiña @Gix @Vorthan @Marek @Parasito @Theron @Brog @Nima @Noah @Vosk @Korin @Lessa @Piloto1 @Piloto2 @Piloto3 @S1G1 @RobotImperial @CazadorRecompensas"
NAVES="@NaveStella @NaveImperial @NaveAliada @NaveNodriza @NaveEsclavista @NavePalacio"
LOC1="@Erdia @CiudadDorada @ParqueLuzagua @Laboratorio @PasillosPalacio @SalaDelOrbe @PlazaPalacio @EspacioErdia"
LOC2="@NodrizaInterior @PlanetaChatarra @FosaApuestas @PlanetaCometas @MinasNiebla @RefugioResistencia @AposentosGeneral"
LOC3="@ErdiaRuinas @SalaTrono"
PROPS="@Orbe @LlaveDeLuz @Brazalete @MonitorMAX @CuchilloLaser @MechaFlores @CollarControl @Proyector @TrajeNuevo @HojaSelka @TanqueSoporte"

# ---------- 00 · Estilo y setup ----------
mk "00_ESTILO_Y_SETUP/Paletas"
mk "00_ESTILO_Y_SETUP/House_Style_SatoshiKon_Ghibli"
mk "00_ESTILO_Y_SETUP/Keyframes_arranque"

# ---------- 01 · Personajes (nombre = @tag del prompt) ----------
for d in $PERS; do mk "01_PERSONAJES/$d"; done

# ---------- 02 · Naves ----------
for d in $NAVES; do mk "02_NAVES/$d"; done

# ---------- 03 · Locaciones (por acto) ----------
for d in $LOC1; do mk "03_LOCACIONES/Acto1/$d"; done
for d in $LOC2; do mk "03_LOCACIONES/Acto2/$d"; done
for d in $LOC3; do mk "03_LOCACIONES/Acto3/$d"; done

# ---------- 04 · Props / objetos ----------
for d in $PROPS; do mk "04_PROPS/$d"; done

# ---------- 05 / 06 / 08 · Keyframes, RAW, exports (por acto) ----------
for a in Acto1 Acto2 Acto3; do mk "05_KEYFRAMES/$a"; mk "06_GENERACIONES_RAW/$a"; mk "08_EXPORTS_CLIPS_FINALES/$a"; done

# ---------- 07 · Audio / SFX ----------
mk "07_AUDIO_SFX"

# ---------- 09 · STORYBOARDS (nuevo) ----------
for a in Acto1 Acto2 Acto3; do mk "09_STORYBOARDS/$a"; done
mk "09_STORYBOARDS/_prompts_por_toma"

# ---------- LÉEME ----------
cat > "$BASE/_LEEME.txt" <<'TXT'
STELLA FUGAZ · "El Nodo de Erdia" — Carpeta de referencias (v2, con @)
======================================================================

CAMBIO EN ESTA VERSIÓN:
- Las carpetas de personaje/nave/locación/prop se llaman EXACTAMENTE como el
  tag del prompt, CON la @ (ej. @StellaRopa, @SalaDelOrbe, @Orbe).
- Nueva carpeta 09_STORYBOARDS para los cuadros del storyboard.

OJO al subir a Higgsfield → Elementos:
  El nombre del ELEMENTO en Higgsfield va SIN la @ (el prompt escribe @StellaRopa,
  pero el elemento se llama "StellaRopa"). La carpeta lleva la @ solo para que
  la reconozcas de un vistazo; al subir, quita la @.

Qué va en cada sitio:
- 00_ESTILO_Y_SETUP  → paletas, estilo (Satoshi Kon + Ghibli), keyframes de arranque.
- 01_PERSONAJES      → una carpeta por @personaje.
- 02_NAVES           → una por @nave.
- 03_LOCACIONES      → @locaciones, ordenadas por acto.
- 04_PROPS           → @objetos (@Orbe, @Brazalete, @HojaSelka, etc.).
- 05_KEYFRAMES       → fotogramas clave por acto.
- 06_GENERACIONES_RAW→ borradores/versiones (historial).
- 07_AUDIO_SFX       → efectos de sonido (la peli es SFX only, sin música).
- 08_EXPORTS_CLIPS_FINALES → videos finales de 15s, por acto.
- 09_STORYBOARDS     → los cuadros del storyboard, por acto (+ _prompts_por_toma).

SECRETOS DE TRAMA (guárdalos aparte para no spoilear el giro):
  @Marek, @Parasito, @SelkaNiña y @NavePalacio son en realidad la misma
  entidad: Vorthan.

Canon de ojos: ÁMBAR → @Stella* y @Naio*.  GRIS-AZUL → @Vera* y @Selka*.
Pelo blanco = voto de la familia.

Total: 65 @elementos (31 personajes · 6 naves · 17 locaciones · 11 props).
TXT

echo ""
echo "✅ Listo. Estructura creada en el Escritorio: Stella_Fugaz_Referencias"
open "$BASE" 2>/dev/null || true
