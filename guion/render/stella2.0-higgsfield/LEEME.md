# 📥 STELLA 2.0 — bajar *AI Film Festival* de Higgsfield al escritorio

Deja `~/Desktop/stella2.0 higgsfield/` con los **551 assets** del proyecto
(cuenta `drawinglion1404`), repartidos en las mismas carpetas que tiene Higgsfield.

Son **tres pasos** y todo corre en tu Mac, en el mismo Chrome donde ya estás logueado.

---

## Paso 1 · Sacar la lista de archivos

1. Abrí el proyecto: `higgsfield.ai/generate/@drawinglion1404/ai-film-festival`
2. Abrí la consola: **⌥⌘J** (Ver → Desarrollador → Consola JavaScript).
3. Abrí `extraer_manifiesto.js`, copiá **todo** el contenido, pegalo en la consola y Enter.
   Aparece un panel negro abajo a la derecha.
4. Para **cada carpeta** del proyecto:
   - hacé clic en la carpeta en la barra lateral;
   - escribí su nombre en el campo **«Carpeta actual»** del panel — tal cual querés que se
     llame en tu disco, con barras para anidar: `Characters/00.Stella`, `Characters/00.Stella/Selected`, `Audio`…
   - pulsá **▶ Escanear esta carpeta** y esperá a que pare (baja sola hasta el final para
     que carguen todas las miniaturas; en las de 200+ tarda un minuto).
5. Cuando estén todas, pulsá **⬇ Exportar manifiesto.tsv**. Se descarga el archivo.

> El script no inventa rutas de API: se engancha a las peticiones que la propia web hace
> y recoge las URLs que van pasando. Por eso hay que abrir cada carpeta — solo ve lo que vos ves.

## Paso 2 · Poner el manifiesto junto al script

Mové el `manifiesto.tsv` descargado a **esta misma carpeta**, al lado de
`descargar_stella2.0.command`.

## Paso 3 · Descargar

Doble clic en **`descargar_stella2.0.command`**.

Si macOS lo bloquea por ser de origen desconocido: clic derecho → **Abrir** → Abrir.
O desde la Terminal: `bash descargar_stella2.0.command`

Al terminar te abre la carpeta y te dice cuántos bajó.

---

## Detalles útiles

- **Se puede reejecutar sin miedo.** Lo ya bajado se salta, así que si se corta internet
  volvés a darle doble clic y sigue donde estaba.
- **Si algo falla**, al final lista los archivos fallidos y quedan en `_descarga.log`
  dentro de la carpeta de destino. Reejecutar reintenta solo esos.
- **`_miniaturas/`**: los pósters de los vídeos se apartan ahí para no ensuciar las
  carpetas. Si no los querés, borrá esas subcarpetas al final.
- **Nombres**: se respeta el nombre de archivo de Higgsfield (su id + extensión).

## Estructura que vas a obtener

Según lo que se ve en el proyecto, con sus números de assets:

```
stella2.0 higgsfield/
├── Audio/
├── Characters/            226
│   ├── 00.Stella/          52   └── Selected/  26
│   ├── 01.Vera/            41
│   ├── 03.Naio/             8
│   ├── 04.Selka/           33
│   ├── 05.Gix/              6
│   ├── 06.Ship Crew/       17
│   ├── 07.Humans/           7
│   ├── 08.Rebels/          13
│   ├── 09.Robots/           8
│   ├── 10.Vorthan/          4
│   ├── 11.Ships & Pilots/  23
│   └── 12.Extras/           9
├── Film Posters/            2
└── …las que queden debajo del scroll en la barra lateral
```

---

## Por qué lo corrés vos y no lo hizo Claude

Mismo motivo que con `../stella-assets/`, y verificado otra vez en esta sesión:

- `higgsfield.ai` y sus dos CDNs devuelven **403 por política de la organización** desde el
  entorno remoto de Claude — no es un fallo de red, y no se reintenta.
- El conector de Higgsfield de esa sesión estaba enlazado a **otra cuenta**
  (`evolvingruler1495`), no a `drawinglion1404`, y un conector OAuth no se cambia
  pasándole un nombre de usuario.
- Ese entorno tampoco ve tu escritorio ni tu Chrome.

Tu Mac tiene las tres cosas: la cuenta, la red y el escritorio.
