#!/bin/bash
# ============================================================
#  STELLA FUGAZ · "El Nodo de Erdia"
#  Crea en tu ESCRITORIO toda la estructura de carpetas para
#  archivar las referencias de la película.
#  → Doble clic para ejecutar (Mac). Si no abre: clic derecho →
#    Abrir. O en Terminal:  bash CREAR_estructura_Stella.command
# ============================================================
set -e
BASE="$HOME/Desktop/Stella_Fugaz_Referencias"
echo "Creando estructura en: $BASE"

mk() { mkdir -p "$BASE/$1"; }

# ---------- 00 · Estilo y setup ----------
mk "00_ESTILO_Y_SETUP/Paletas"
mk "00_ESTILO_Y_SETUP/House_Style_SatoshiKon_Ghibli"
mk "00_ESTILO_Y_SETUP/Keyframes_arranque"

# ---------- 01 · Personajes (nombre de carpeta = @elemento) ----------
for d in StellaRopa StellaArmadura StellaPeloCorto StellaTeñida; do mk "01_PERSONAJES/Stella/$d"; done
for d in VeraRopa VeraArmadura VeraEncapuchada; do mk "01_PERSONAJES/Vera/$d"; done
for d in Naio NaioEsclavo NaioRescatado; do mk "01_PERSONAJES/Naio/$d"; done
for d in SelkaBebe SelkaCadete SelkaGeneral SelkaNiña_🔒; do mk "01_PERSONAJES/Selka/$d"; done
mk "01_PERSONAJES/Gix"
for d in Vorthan Marek_🔒 Parasito_🔒; do mk "01_PERSONAJES/Vorthan_SECRETO/$d"; done
for d in Theron Brog Nima Noah Vosk; do mk "01_PERSONAJES/Tripulacion_Theron/$d"; done
for d in Korin Lessa Piloto1 Piloto2 Piloto3; do mk "01_PERSONAJES/Resistencia/$d"; done
for d in S1G1 RobotImperial CazadorRecompensas; do mk "01_PERSONAJES/Enemigos/$d"; done

# ---------- 02 · Naves ----------
for d in NaveStella NaveImperial NaveAliada NaveNodriza NaveEsclavista NavePalacio_🔒; do mk "02_NAVES/$d"; done

# ---------- 03 · Locaciones (por acto) ----------
for d in Erdia CiudadDorada ParqueLuzagua Laboratorio PasillosPalacio SalaDelOrbe PlazaPalacio EspacioErdia; do mk "03_LOCACIONES/Acto1/$d"; done
for d in NodrizaInterior PlanetaChatarra FosaApuestas PlanetaCometas MinasNiebla RefugioResistencia AposentosGeneral; do mk "03_LOCACIONES/Acto2/$d"; done
for d in ErdiaRuinas SalaTrono; do mk "03_LOCACIONES/Acto3/$d"; done

# ---------- 04 · Props / objetos ----------
for d in Orbe LlaveDeLuz Brazalete MonitorMAX CuchilloLaser MechaFlores CollarControl Proyector TrajeNuevo HojaSelka TanqueSoporte; do mk "04_PROPS/$d"; done

# ---------- 05 · Keyframes por acto ----------
for a in Acto1 Acto2 Acto3; do mk "05_KEYFRAMES/$a"; done

# ---------- 06 · Generaciones RAW (borradores / historial) ----------
for a in Acto1 Acto2 Acto3; do mk "06_GENERACIONES_RAW/$a"; done

# ---------- 07 · Audio / SFX ----------
mk "07_AUDIO_SFX"

# ---------- 08 · Exports finales de clips (video 15s) ----------
for a in Acto1 Acto2 Acto3; do mk "08_EXPORTS_CLIPS_FINALES/$a"; done

# ---------- LÉEME ----------
cat > "$BASE/_LEEME.txt" <<'TXT'
STELLA FUGAZ · "El Nodo de Erdia" — Carpeta de referencias
==========================================================

REGLA DE ORO: el nombre de cada carpeta de personaje/nave/locación/prop
es EXACTAMENTE el nombre del @elemento. Cuando subas la lámina a
Higgsfield → Elementos, guárdala con ese mismo nombre (sin el @) y los
prompts la autoconectan.

Qué va en cada sitio:
- 00_ESTILO_Y_SETUP  → paletas, referencias de estilo (Satoshi Kon + Ghibli), keyframes de arranque.
- 01_PERSONAJES      → una carpeta por versión del personaje (ej. Stella tiene 4).
- 02_NAVES           → cada nave.
- 03_LOCACIONES      → establishing de cada locación, ordenadas por acto.
- 04_PROPS           → objetos (Orbe, Brazalete, HojaSelka, etc.).
- 05_KEYFRAMES       → fotogramas clave por acto.
- 06_GENERACIONES_RAW→ borradores/versiones que vas generando (el "historial").
- 07_AUDIO_SFX       → efectos de sonido (la peli es SFX only, sin música).
- 08_EXPORTS_CLIPS_FINALES → los videos finales de 15s, por acto.

🔒 = SECRETO de trama (Marek, Parásito, SelkaNiña, NavePalacio son Vorthan).
Guárdalos como elementos aparte para no spoilear el giro.

Total: 63 @elementos (29 personajes · 6 naves · 17 locaciones · 11 props).
Consejo: dentro de cada carpeta de personaje puedes tener subcarpetas
"01_final", "02_variantes", "03_descartes" si quieres ordenar versiones.
TXT

echo ""
echo "✅ Listo. Estructura creada en el Escritorio: Stella_Fugaz_Referencias"
open "$BASE" 2>/dev/null || true
