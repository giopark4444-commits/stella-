# 📥 STELLA 2.0 — bajar todo lo de Higgsfield al escritorio

Deja `~/Desktop/stella2.0 higgsfield/` con los **979 archivos** de la cuenta
`drawinglion1404` (`user_3Hl0XObMDaFT2IDolV9XkUACEpZ`).

El `manifiesto.tsv` ya está hecho y **verificado**. Solo falta ejecutarlo.

---

## Un solo paso

Doble clic en **`descargar_stella2.0.command`**.

Si macOS lo bloquea: clic derecho → **Abrir** → Abrir. Desde Terminal: `bash descargar_stella2.0.command`

- **Reejecutable**: lo ya bajado se salta; si se corta internet, doble clic otra vez y sigue.
- **Si algo falla**: lista los fallidos al terminar y los deja en `_descarga.log`. Reejecutar reintenta solo esos.

## Qué vas a obtener

```
stella2.0 higgsfield/
├── imagenes/2026-08/    400  ┐
├── imagenes/2026-09/     71  │ 657 generaciones
├── videos/2026-08/       35  │ (471 PNG + 186 MP4)
├── videos/2026-09/      151  ┘
├── subidas/imagenes/    314  ┐ 322 archivos que subiste vos
└── subidas/videos/        8  ┘ (referencias, fuentes)
```

Junto a esto va **`indice.csv`**: una fila por archivo con carpeta, tipo, fecha y —en las
generaciones que los llevan— **los elementos de referencia usados** (`char_lessa`, `robot-g45`,
`loc_facade`…). Sirve para localizar piezas por personaje o locación.

---

## ✅ Repaso de completitud (2026-09-08)

Se verificó que **lo que está online en la cuenta esté completo**, por dos vías independientes:

| Fuente | Resultado | Cómo se comprobó |
|---|---|---|
| Generaciones de imagen | **471** | Paginado sin filtro (657) y de nuevo filtrando por tipo. **0 faltantes** |
| Generaciones de vídeo | **186** | Igual, contraste cruzado. **0 faltantes** |
| Subidas de imagen | **314** | Paginado hasta `next_cursor: null` |
| Subidas de vídeo | **8** | Paginado hasta `next_cursor: null` |
| Generaciones de audio | **0** | La API devuelve lista vacía |
| Subidas de audio | **0** | La API devuelve lista vacía |
| Elements | sin archivos nuevos | Su media es o una generación o una subida ya incluida (comprobado por muestreo) |
| Generaciones 3D | **no verificable** | La API da error de servidor en las dos consultas |

**Total: 979 archivos**, sin URLs repetidas, todas apuntando a la cuenta correcta.

### Dos cosas que no cuadran, y por qué

**La carpeta `Audio` del proyecto sale vacía.** El conector no devuelve ningún audio, ni generado
ni subido. O está vacía, o su contenido no se expone por esta vía.

**Tu proyecto marca 551 assets y aquí hay 979.** No es contradicción: 551 es lo que queda **dentro
del proyecto** *AI Film Festival*; 979 es **todo lo que sigue online en la cuenta**, incluyendo lo
que borraste del proyecto pero no de la cuenta, más las subidas. Como pediste, prima que lo online
esté completo. Nada se descarta por no estar ya en el proyecto.

## ⚠️ Lo que sigue sin poder darse: las carpetas del proyecto

El conector expone el historial, la mediateca y los Elements del workspace, pero **no los proyectos
ni sus carpetas**. Por eso no hay `Characters/00.Stella` ni `06.Ship Crew`: agrupé por origen, tipo
y mes, que es lo único derivable.

Si querés las carpetas exactas, usá `extraer_manifiesto.js` (se pega en la consola de Chrome con el
proyecto abierto). Su manifiesto sustituye a este y el `.command` funciona igual. Cotejá con
`indice.csv` que no falte nada.

## Por qué lo corrés vos

`higgsfield.ai` y sus CDNs responden **403 por política de la organización** desde el entorno remoto
de Claude, que además no ve tu escritorio. El conector va por otro canal, y por eso el inventario sí
se pudo hacer aquí. Bajar los bytes, no.
