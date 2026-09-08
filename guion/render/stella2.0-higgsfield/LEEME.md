# 📥 STELLA 2.0 — bajar los assets de Higgsfield al escritorio

Deja `~/Desktop/stella2.0 higgsfield/` con los **657 assets** de la cuenta
`drawinglion1404` (`user_3Hl0XObMDaFT2IDolV9XkUACEpZ`): **471 imágenes PNG y 186 vídeos MP4**.

El `manifiesto.tsv` **ya está hecho** — se generó vía el conector de Higgsfield, con las URLs
de los originales en máxima calidad (no miniaturas). Solo falta ejecutarlo.

---

## Un solo paso

Doble clic en **`descargar_stella2.0.command`**.

Si macOS lo bloquea por origen desconocido: clic derecho → **Abrir** → Abrir.
Desde Terminal: `bash descargar_stella2.0.command`

Al terminar abre la carpeta y dice cuántos bajó.

- **Reejecutable sin miedo**: lo ya bajado se salta, así que si se corta internet, doble clic otra vez y sigue.
- **Si algo falla**: al final lista los fallidos, y quedan en `_descarga.log` dentro de la carpeta destino. Reejecutar reintenta solo esos.

---

## Qué vas a obtener

```
stella2.0 higgsfield/
├── imagenes/
│   ├── 2026-08/   400 png
│   └── 2026-09/    71 png
├── videos/
│   ├── 2026-08/    35 mp4
│   └── 2026-09/   151 mp4
└── _descarga.log
```

Los nombres son los originales de Higgsfield (`hf_AAAAMMDD_HHMMSS_<id>`), así que quedan
ordenados cronológicamente dentro de cada carpeta.

Junto a este README va **`indice.csv`**, con una fila por asset: carpeta, archivo, tipo, fecha
y **los elementos de referencia que usó** (`char_lessa`, `robot-g45`, `loc_facade`…). 186 de los
657 los llevan. Sirve para localizar piezas por personaje o locación, y para reorganizar después.

---

## ⚠️ Por qué NO están las carpetas de tu proyecto

Pediste la estructura tal cual está en Higgsfield (`Characters/00.Stella`, `06.Ship Crew`…).
**El conector no expone los proyectos ni sus carpetas** — solo el historial de generaciones y
los Elements del workspace. Así que agrupé por lo único que sí puedo derivar: tipo y mes.

Si querés las carpetas exactas, está `extraer_manifiesto.js`: se pega en la consola de Chrome
con el proyecto abierto, vas marcando cada carpeta y le das a Escanear, y exporta un
`manifiesto.tsv` con las carpetas reales. Ese manifiesto sustituye a este y el `.command`
funciona igual. Con `indice.csv` podés cotejar que no falte nada.

Los conteos tampoco coinciden del todo: tu proyecto marca 551 assets y el historial da 657.
La diferencia es normal — el historial incluye generaciones que no metiste en el proyecto.

## Por qué lo corrés vos y no lo hizo Claude

`higgsfield.ai` y sus CDNs responden **403 por política de la organización** desde el entorno
remoto de Claude, y ese entorno no ve tu escritorio. El conector sí funciona (va por otro
canal), y por eso el inventario y las URLs sí se pudieron sacar aquí. Bajar los bytes, no.
