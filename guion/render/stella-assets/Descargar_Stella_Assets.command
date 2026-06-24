#!/usr/bin/env bash
# Doble-clic en Mac para descargar TODOS los assets a ~/Desktop/stella assets/
# (La 1ª vez, si macOS bloquea: clic derecho → Abrir → Abrir.)
cd "$(dirname "$0")"
bash download_stella_assets.sh
echo ""
read -n 1 -s -r -p "Listo. Pulsa cualquier tecla para cerrar esta ventana..."
echo ""
