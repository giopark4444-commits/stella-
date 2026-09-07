#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# STELLA 2.0 · descarga el proyecto "AI Film Festival" de Higgsfield
# (cuenta drawinglion1404) a ~/Desktop/stella2.0 higgsfield/, respetando las
# carpetas del proyecto.
#
# Uso: doble clic en el Finder, o  bash descargar_stella2.0.command
#
# Lee el manifiesto  manifiesto.tsv  que está junto a este script:
#     carpeta <TAB> nombre_archivo <TAB> url
# Se puede volver a ejecutar cuantas veces haga falta: lo ya bajado se salta,
# así que si se corta la conexión basta con volver a lanzarlo.
# ---------------------------------------------------------------------------
set -uo pipefail
cd "$(dirname "$0")"

DEST="$HOME/Desktop/stella2.0 higgsfield"
MANIFIESTO="${1:-manifiesto.tsv}"
LOG="$DEST/_descarga.log"

if [ ! -f "$MANIFIESTO" ]; then
  echo "✗ No encuentro «$MANIFIESTO» junto a este script."
  echo "  Generalo primero con extraer_manifiesto.js (ver LEEME.md, paso 1)."
  read -n1 -r -p "Pulsa una tecla para cerrar…"; exit 1
fi

mkdir -p "$DEST"
: > "$LOG"
total=$(grep -cve '^\s*#' -e '^\s*$' "$MANIFIESTO")
ok=0; salt=0; fallo=0; n=0
fallidos=()

printf '\n📥 STELLA 2.0 · %s archivos → %s\n\n' "$total" "$DEST"

while IFS=$'\t' read -r carpeta nombre url; do
  case "$carpeta" in ''|\#*) continue ;; esac
  [ -z "${url:-}" ] && continue
  n=$((n+1))

  destino="$DEST/$carpeta"
  mkdir -p "$destino"
  archivo="$destino/$nombre"

  # ya está y no está vacío -> se salta (permite reanudar)
  if [ -s "$archivo" ]; then
    salt=$((salt+1))
    printf '\r[%4d/%4d] ⏭  %-52.52s' "$n" "$total" "$carpeta/$nombre"
    echo "SALTADO $carpeta/$nombre" >> "$LOG"
    continue
  fi

  printf '\r[%4d/%4d] ⬇  %-52.52s' "$n" "$total" "$carpeta/$nombre"
  if curl -fsSL --retry 4 --retry-delay 2 --retry-connrefused \
          --connect-timeout 20 --max-time 600 \
          "$url" -o "$archivo.parcial" 2>>"$LOG"; then
    mv -f "$archivo.parcial" "$archivo"
    ok=$((ok+1))
    echo "OK      $carpeta/$nombre" >> "$LOG"
  else
    rm -f "$archivo.parcial"
    fallo=$((fallo+1))
    fallidos+=("$carpeta/$nombre")
    echo "FALLO   $carpeta/$nombre  <- $url" >> "$LOG"
  fi
done < "$MANIFIESTO"

printf '\r%-72s\n\n' " "
echo "──────────────────────────────────────────"
printf '  ✅ descargados : %d\n  ⏭  ya estaban  : %d\n  ❌ fallidos    : %d\n' "$ok" "$salt" "$fallo"
echo "──────────────────────────────────────────"

if [ "$fallo" -gt 0 ]; then
  echo
  echo "Fallaron estos (volvé a ejecutar el script y solo reintenta estos):"
  printf '  · %s\n' "${fallidos[@]}"
fi

echo
echo "📄 Detalle en: $LOG"
du -sh "$DEST" 2>/dev/null | awk '{print "💾 Tamaño total: " $1}'
command -v open >/dev/null && open "$DEST"
echo
read -n1 -r -p "Listo. Pulsa una tecla para cerrar…"
