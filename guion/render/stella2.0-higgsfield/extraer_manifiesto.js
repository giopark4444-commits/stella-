/* ===========================================================================
   STELLA 2.0 · extractor de manifiesto de Higgsfield
   ---------------------------------------------------------------------------
   Se pega en la consola de Chrome con el proyecto "AI Film Festival" abierto
   (higgsfield.ai/generate/@drawinglion1404/ai-film-festival), estando logueado.

   Qué hace: se engancha a las peticiones que la propia web hace y va juntando
   las URLs de los assets que se van cargando, etiquetadas con la carpeta que
   tengas abierta. No usa ninguna API privada ni adivina rutas: recoge lo que
   la página ya pide por su cuenta, así que sigue funcionando aunque Higgsfield
   cambie su backend.

   Flujo: pegar → abrir una carpeta → ▶ Escanear → repetir por cada carpeta →
          ⬇ Exportar. Sale un manifiesto.tsv.
   =========================================================================== */
(() => {
  if (window.__HF_STELLA) { window.__HF_STELLA.panel(); return; }

  const CDN = /https?:\/\/[a-z0-9]+\.cloudfront\.net\/[^\s"'\\)]+/gi;
  const RAW = 'd8j0ntlcm91z4';                    // CDN de originales
  const EXT_OK = /\.(mp4|mov|webm|png|jpe?g|webp|gif|mp3|wav|m4a)$/i;

  const assets = new Map();                       // uuid -> {url, carpeta, ext}
  let carpeta = 'Sin_carpeta';

  const uuidDe = (u) => (u.split('/').pop() || '').replace(/\.[^.]+$/, '');
  const extDe  = (u) => ((u.match(EXT_OK) || [''])[0] || '').toLowerCase();

  function guardar(url, esMini = false) {
    url = url.split('?')[0];
    if (!EXT_OK.test(url)) return;
    const id = uuidDe(url);
    if (!id) return;
    const previo = assets.get(id);
    // preferimos el original sobre la miniatura
    if (previo && !(url.includes(RAW) && !previo.url.includes(RAW))) return;
    assets.set(id, { url, carpeta, ext: extDe(url), mini: esMini && !url.includes(RAW) });
    pintar();
  }

  // Recorre el JSON mirando los NOMBRES de las claves: así sabemos si una URL
  // es el asset de verdad o solo el poster de un vídeo.
  const CLAVE_MINI = /thumb|preview|poster|cover|icon/i;
  function caminar(v, clave = '') {
    if (typeof v === 'string') { if (CDN.test(v)) { CDN.lastIndex = 0; guardar(v, CLAVE_MINI.test(clave)); } return; }
    if (Array.isArray(v)) { v.forEach((x) => caminar(x, clave)); return; }
    if (v && typeof v === 'object') { for (const k in v) caminar(v[k], k); }
  }

  const rascar = (txt) => {
    try { caminar(JSON.parse(txt)); return; } catch (e) {}
    const m = String(txt).match(CDN);      // no era JSON: regex a secas
    if (m) m.forEach((u) => guardar(u, false));
  };

  // --- enganche a fetch -----------------------------------------------------
  const fetchOrig = window.fetch;
  window.fetch = async function (...args) {
    const res = await fetchOrig.apply(this, args);
    res.clone().text().then(rascar).catch(() => {});
    return res;
  };

  // --- enganche a XHR -------------------------------------------------------
  const abrirOrig = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (...args) {
    this.addEventListener('load', () => { try { rascar(this.responseText); } catch (e) {} });
    return abrirOrig.apply(this, args);
  };

  // --- barrido del DOM (lo ya pintado) --------------------------------------
  function barrerDOM() {
    document.querySelectorAll('img[src],video[src],source[src],video[poster],a[href]')
      .forEach((el) => ['src', 'href', 'poster'].forEach((a) => {
        if (!el[a]) return;
        const esMini = (a === 'poster') || (a === 'src' && el.tagName === 'IMG');
        String(el[a]).match(CDN)?.forEach((u) => guardar(u, esMini));
      }));
  }

  // --- scroll automático para forzar la carga perezosa ----------------------
  function contenedorScroll() {
    let mejor = null, max = 0;
    document.querySelectorAll('div,main,section').forEach((el) => {
      const s = el.scrollHeight - el.clientHeight;
      if (s > max && el.clientHeight > 300 && getComputedStyle(el).overflowY.match(/auto|scroll/)) {
        max = s; mejor = el;
      }
    });
    return mejor || document.scrollingElement;
  }

  async function escanear() {
    const cont = contenedorScroll();
    const antes = assets.size;
    let quieto = 0, ultimo = -1;
    estado(`Escaneando «${carpeta}»…`);
    for (let i = 0; i < 400 && quieto < 6; i++) {
      cont.scrollTop = cont.scrollHeight;
      await new Promise((r) => setTimeout(r, 450));
      barrerDOM();
      if (assets.size === ultimo) quieto++; else { quieto = 0; ultimo = assets.size; }
    }
    cont.scrollTop = 0;
    estado(`«${carpeta}»: +${assets.size - antes} nuevos · ${assets.size} en total`);
  }

  // --- exportar -------------------------------------------------------------
  function exportar() {
    const filas = ['# carpeta\tnombre\turl'];
    const cuenta = {};
    for (const [id, a] of assets) {
      let c = a.carpeta.replace(/^\/+|\/+$/g, '') || 'Sin_carpeta';
      if (a.mini) c += '/_miniaturas';
      cuenta[c] = (cuenta[c] || 0) + 1;
      filas.push(`${c}\t${id}${a.ext}\t${a.url}`);
    }
    const blob = new Blob([filas.join('\n') + '\n'], { type: 'text/tab-separated-values' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'manifiesto.tsv';
    a.click();
    console.table(cuenta);
    estado(`Exportados ${assets.size} assets.`);
  }

  // --- panel ----------------------------------------------------------------
  let caja, txtEstado;
  function panel() {
    if (caja) { caja.style.display = 'block'; return; }
    caja = document.createElement('div');
    caja.style.cssText = `position:fixed;z-index:2147483647;right:16px;bottom:16px;width:290px;
      background:#111;color:#eee;font:13px/1.45 system-ui,sans-serif;padding:14px;
      border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,.5)`;
    caja.innerHTML = `
      <div style="font-weight:600;margin-bottom:8px">📥 STELLA 2.0 · extractor</div>
      <label style="display:block;font-size:11px;opacity:.7">Carpeta actual</label>
      <input id="hfCarpeta" value="${carpeta}" style="width:100%;box-sizing:border-box;margin:4px 0 10px;
        padding:6px;border-radius:6px;border:1px solid #444;background:#1c1c1c;color:#eee">
      <button id="hfScan"  style="width:100%;padding:7px;margin-bottom:6px;border:0;border-radius:6px;
        background:#2d7;color:#000;font-weight:600;cursor:pointer">▶ Escanear esta carpeta</button>
      <button id="hfExport" style="width:100%;padding:7px;border:0;border-radius:6px;
        background:#48f;color:#fff;font-weight:600;cursor:pointer">⬇ Exportar manifiesto.tsv</button>
      <div id="hfEstado" style="margin-top:9px;font-size:11px;opacity:.8">0 assets</div>`;
    document.body.appendChild(caja);
    txtEstado = caja.querySelector('#hfEstado');
    const inp = caja.querySelector('#hfCarpeta');
    inp.oninput = () => { carpeta = inp.value.trim() || 'Sin_carpeta'; };
    caja.querySelector('#hfScan').onclick = escanear;
    caja.querySelector('#hfExport').onclick = exportar;
  }
  const estado = (t) => { if (txtEstado) txtEstado.textContent = t; console.log('[STELLA]', t); };
  const pintar = () => { if (txtEstado && !/Escaneando/.test(txtEstado.textContent)) estado(`${assets.size} assets`); };

  panel();
  barrerDOM();
  window.__HF_STELLA = { assets, escanear, exportar, panel,
    carpeta: (n) => { carpeta = n; caja.querySelector('#hfCarpeta').value = n; } };
  console.log('%c[STELLA] Extractor activo. Abrí una carpeta y pulsá «Escanear».',
              'color:#2d7;font-weight:600');
})();
