#!/usr/bin/env python3
"""
prompts_guion_20s.py — genera prompts que son EL GUION TAL CUAL, troceado en
bloques de ~20 segundos, con las menciones @[NOMBRE](uuid) y el bloque tecnico
pegado al final. Nada de campos Style/Setting/Shot: texto de guion, literal.

Fuente del texto : guion/GUION_P1_v2_DIALOGOS_EN_SEEDANCE.md (hibrido)
Fuente del tiempo: guion/PRODUCCION_BLOQUES_20S.csv (duracion real por secuencia)

El troceo NO se estima a ojo: cada secuencia tiene una duracion real conocida,
y el peso de cada parrafo (por palabras) se escala para que la suma de la
secuencia cuadre con esa duracion. Asi los cortes caen en frontera natural
—nunca parten un bloque de dialogo— y los totales siguen siendo los de la
pelicula (48:27).

Uso: python3 tools/prompts_guion_20s.py
"""
import re
import csv
import json
import html
import collections

HIBRIDO = "guion/02_guiones/GUION_P1_v2_DIALOGOS_EN_SEEDANCE.md"
BLOQUES = "guion/04_produccion/PRODUCCION_BLOQUES_20S.csv"
SALIDA_HTML = "guion/06_web/PROMPTS_GUION_20S.html"
SALIDA_MD = "guion/03_prompts/PROMPTS_GUION_20S.md"

SEGUNDOS = 20

# UUID que Gio ya dio. El resto se rellena desde la propia pagina y queda
# guardado en el navegador; NO se inventan, una id falsa es una referencia rota.
IDS_CONOCIDOS = {
    "VERA":   "440a3221-f4a0-48fb-aac8-12f6e67b84f7",
    "SELKA":  "79eea014-b2c6-4e92-af08-59762f7d4eb4",
    "STELLA": "14163f5a-be57-4e54-9d14-706edde3bddb",
}

PERSONAJES = ["STELLA", "VERA", "SELKA", "NAIO", "GIX", "VORTHAN", "THERON",
              "VOSK", "KORIN", "LESSA", "MAREK", "BROG", "NIMA", "NOAH", "S1G1"]

# Bloque tecnico que va AL FINAL de cada prompt (formato de Gio, con la
# ortografia corregida: "Miyazaki", "sound design").
ESTILO = ("Style: hand-painted 2D anime, painterly watercolor backgrounds, "
          "cinematic composition and mood, expressive character acting, fluid "
          "motion, film-grade lighting, soft grain. Miyazaki style and Satoshi "
          "Kon mood. 21:9, 20s.")
AUDIO = "Audio: Just rich sound design, no music at all."
# Continuidad: solo se emite si el personaje aparece en ESE bloque.
CONTINUIDAD = {
    "STELLA": "@[STELLA] siempre tiene su brazalete en el brazo izquierdo.",
    "GIX":    "@[GIX] es siempre azul-luzagua y oro cálido, nunca gris metálico.",
}


# --------------------------------------------------------------------------
def duracion_por_secuencia():
    """{n_secuencia: segundos} a partir de los 172 bloques ya calculados."""
    total = collections.Counter()
    with open(BLOQUES, encoding="utf-8") as fh:
        for fila in csv.DictReader(fh):
            m = re.search(r"SEC\s*(\d+)", fila["secuencia"])
            if m:
                total[int(m.group(1))] += int(fila["dur_seg"])
    return dict(total)


def secuencias_del_guion():
    """[(n, titulo, [parrafos])] leyendo el hibrido."""
    txt = open(HIBRIDO, encoding="utf-8").read()
    partes = re.split(r"(?m)^##\s+SEC\.\s*(\d+)\s*—\s*([^\n]+)$", txt)
    salida = []
    for i in range(1, len(partes), 3):
        n = int(partes[i])
        titulo = partes[i + 1].strip()
        cuerpo = partes[i + 2]
        parrafos = []
        for p in re.split(r"\n\s*\n", cuerpo):
            p = p.strip()
            if not p or p.startswith(">") or set(p) <= set("-—* "):
                continue
            parrafos.append(p)
        if parrafos:
            salida.append((n, titulo, parrafos))
    return salida


def es_dialogo(par):
    """Cabecera de dialogo = una linea que contiene SOLO el nombre.

    Ojo: "**@BROG** y @Stella, sentados frente a..." es ACCION, aunque empiece
    con un nombre en negrita. Confundirlas hacia que no se partieran nunca y
    dejaba bloques de 33s.
    """
    primera = par.split("\n")[0].strip()
    return bool(re.fullmatch(r"\*\*@[A-ZÁÉÍÓÚÑ0-9 .()']+\*\*", primera)) and "\n" in par


def limpiar(par):
    """Guion -> texto plano de prompt, conservando las palabras tal cual."""
    t = par
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t, flags=re.S)   # negrita fuera
    t = re.sub(r"\*(.+?)\*", r"\1", t, flags=re.S)       # cursiva fuera
    t = t.replace("`", "")
    # @Nombre -> @[NOMBRE](§NOMBRE§); el marcador lo sustituye la pagina
    def mencion(m):
        nombre = m.group(1).upper()
        return f"@[{nombre}](§{nombre}§)" if nombre in PERSONAJES else m.group(0)
    t = re.sub(r"@([A-Za-zÁÉÍÓÚÑáéíóúñ0-9]+)", mencion, t)
    return t.strip()


def personajes_en(texto):
    return [p for p in PERSONAJES if f"@[{p}]" in texto]


# props y elementos con hoja de referencia propia; se detectan por su nombre
# en el texto para decirle a Gio que laminas adjuntar en ese bloque
ELEMENTOS = {
    "MECHA": r"\bMECHA\b",
    "Orbe": r"\bOrbe\b",
    "brazalete": r"\bbrazalete\b",
    "luzagua": r"\bluzagua\b",
    "Llave de luz": r"\bllave de luz\b",
    "Cuchillo láser": r"\bcuchillo l[áa]ser\b",
}


def elementos_en(texto):
    return [n for n, pat in ELEMENTOS.items() if re.search(pat, texto, re.I)]


def trocear():
    dur_sec = duracion_por_secuencia()
    bloques = []
    for n, titulo, parrafos in secuencias_del_guion():
        objetivo = dur_sec.get(n)
        palabras = [max(1, len(p.split())) for p in parrafos]
        if objetivo:
            escala = objetivo / sum(palabras)          # calibrado al tiempo real
        else:
            escala = 1 / 2.6                            # ~2.6 palabras por segundo
        pesos = [w * escala for w in palabras]

        # Un parrafo de accion largo ya se pasa de 20s el solo: se parte por
        # FRASES (el texto sigue siendo literal). Los bloques de dialogo no se
        # parten nunca: separar la replica de su personaje lo estropea.
        unidades = []
        for par, peso in zip(parrafos, pesos):
            if peso <= SEGUNDOS or es_dialogo(par):
                unidades.append((par, peso))
                continue
            frases = re.findall(r"[^.!?]+[.!?]*\s*", par)
            grupo, peso_grupo = [], 0.0
            for fr in frases:
                pf = max(1, len(fr.split())) * escala
                if grupo and peso_grupo + pf > SEGUNDOS:
                    unidades.append(("".join(grupo).strip(), peso_grupo))
                    grupo, peso_grupo = [], 0.0
                grupo.append(fr)
                peso_grupo += pf
            if grupo:
                unidades.append(("".join(grupo).strip(), peso_grupo))

        actual, dur_actual = [], 0.0
        for par, peso in unidades:
            # se cierra ANTES de pasarse de 20s, no despues
            if actual and dur_actual + peso > SEGUNDOS:
                bloques.append((n, titulo, actual, dur_actual))
                actual, dur_actual = [], 0.0
            actual.append(par)
            dur_actual += peso
        if actual:
            # la cola de una secuencia puede quedar muy corta; se funde con el
            # bloque anterior de la MISMA secuencia en vez de dejar un trozo
            # de 5s suelto (nunca se cruza de secuencia).
            if dur_actual < 8 and bloques and bloques[-1][0] == n:
                pn, pt, pp, pd = bloques.pop()
                bloques.append((pn, pt, pp + actual, pd + dur_actual))
            else:
                bloques.append((n, titulo, actual, dur_actual))
    return bloques


def texto_prompt(parrafos):
    cuerpo = "\n".join(limpiar(p) for p in parrafos)
    pers = personajes_en(cuerpo)
    lineas = [cuerpo, "", ESTILO, AUDIO]
    for p in pers:
        if p in CONTINUIDAD:
            lineas.append(CONTINUIDAD[p].replace(f"@[{p}]", f"@[{p}](§{p}§)"))
    refs = [f"@[{p}](§{p}§)" for p in pers] + elementos_en(cuerpo)
    if refs:
        lineas.append("Referencias a adjuntar: " + ", ".join(refs))
    return "\n".join(lineas)


# --------------------------------------------------------------------------
def main():
    bloques = trocear()
    total = sum(b[3] for b in bloques)

    # ---------- markdown ----------
    md = ["# PROMPTS · EL GUION TROCEADO EN 20s",
          f"## {len(bloques)} bloques · {int(total)//60}:{int(total)%60:02d} de película",
          "",
          "> Es el guion híbrido **tal cual** (acción en español, diálogos en inglés),",
          "> partido en bloques de ~20s. Ningún bloque parte un párrafo ni cruza de secuencia.",
          "> El tiempo no está estimado a ojo: cada secuencia se calibra con su duración real",
          "> de `PRODUCCION_BLOQUES_20S.csv`.",
          "",
          "> Los `§NOMBRE§` son los UUID que faltan. Rellénalos en la página HTML y quedan guardados.",
          ""]
    sec_actual = None
    for i, (n, titulo, parrafos, dur) in enumerate(bloques, 1):
        if n != sec_actual:
            md += ["", f"## SEC. {n} — {titulo}", ""]
            sec_actual = n
        md += [f"### BLOQUE {i} · ~{dur:.0f}s", "", "```", texto_prompt(parrafos), "```", ""]
    open(SALIDA_MD, "w", encoding="utf-8").write("\n".join(md))

    # ---------- html ----------
    datos = []
    sec_actual = None
    for i, (n, titulo, parrafos, dur) in enumerate(bloques, 1):
        datos.append({"i": i, "sec": n, "titulo": titulo,
                      "dur": round(dur), "txt": texto_prompt(parrafos)})
    open(SALIDA_HTML, "w", encoding="utf-8").write(pagina(datos, total))
    print(f"{len(bloques)} bloques · {int(total)//60}:{int(total)%60:02d}")
    print(f"  → {SALIDA_HTML}")
    print(f"  → {SALIDA_MD}")
    faltan = sorted(set(PERSONAJES) - set(IDS_CONOCIDOS))
    print(f"  UUID por rellenar en la página: {', '.join(faltan)}")


def pagina(datos, total):
    secs = []
    vista = None
    for d in datos:
        if d["sec"] != vista:
            secs.append(f'<h2 class="sec" id="s{d["sec"]}">SEC. {d["sec"]} — {html.escape(d["titulo"])}</h2>')
            vista = d["sec"]
        secs.append(
            f'<div class="clip" data-i="{d["i"]}">'
            f'<div class="ch"><span class="cid">BLOQUE {d["i"]}</span>'
            f'<span class="cdur">~{d["dur"]}s</span>'
            f'<button class="cp">⧉ Copiar</button></div>'
            f'<pre class="txt">{html.escape(d["txt"])}</pre></div>')
    campos = "".join(
        f'<label><span>@{p}</span><input data-p="{p}" value="{IDS_CONOCIDOS.get(p,"")}" '
        f'placeholder="pega aquí el UUID de {p}"></label>' for p in PERSONAJES)
    return PLANTILLA.replace("{{CUERPO}}", "\n".join(secs)) \
                    .replace("{{CAMPOS}}", campos) \
                    .replace("{{N}}", str(len(datos))) \
                    .replace("{{DUR}}", f"{int(total)//60}:{int(total)%60:02d}") \
                    .replace("{{IDS}}", json.dumps(IDS_CONOCIDOS))


PLANTILLA = r"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Stella Fugaz · Prompts del guion · 20s</title>
<style>
:root{--gold:#e8c27a;--green:#7fe0a3;--txt:#eef0f5;--mut:#9aa3b2;--line:#262b36;--card:#141821}
*{box-sizing:border-box}html,body{margin:0}
body{background:#0b0d12;color:var(--txt);font:16px/1.65 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
header{position:sticky;top:0;z-index:5;background:#0b0d12ee;backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:14px 22px}
header b{color:var(--gold);letter-spacing:2px;font-size:13px}
header .m{color:var(--mut);font-size:12px;margin-left:10px}
.wrap{max-width:900px;margin:0 auto;padding:26px 22px 80px}
a.back{color:var(--mut);text-decoration:none;font-size:13px;border:1px solid var(--line);border-radius:20px;padding:5px 13px}
a.back:hover{color:var(--gold);border-color:var(--gold)}
.ids{background:#101a16;border:1px solid #1e3329;border-left:3px solid var(--green);border-radius:12px;padding:18px 20px;margin:22px 0}
.ids h3{margin:0 0 6px;font-size:14px;color:var(--green);letter-spacing:.4px}
.ids p{margin:0 0 14px;color:#c3ccd6;font-size:13.5px}
.ids .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:8px}
.ids label{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--mut)}
.ids label span{min-width:74px;color:var(--gold);font-weight:600}
.ids input{flex:1;min-width:0;background:#0a0f0d;border:1px solid #23303a;border-radius:7px;color:var(--txt);padding:6px 9px;font:12px ui-monospace,Menlo,monospace}
.ids input:focus{outline:none;border-color:var(--green)}
.ids .ok{color:var(--green)}
h2.sec{font-size:13px;letter-spacing:2.5px;text-transform:uppercase;color:var(--mut);margin:34px 0 12px;border-bottom:1px solid var(--line);padding-bottom:8px}
.clip{background:var(--card);border:1px solid var(--line);border-radius:13px;margin-bottom:14px;overflow:hidden}
.ch{display:flex;align-items:center;gap:10px;padding:11px 15px;border-bottom:1px solid var(--line);background:#11151d}
.cid{color:var(--gold);font-weight:700;font-size:12px;letter-spacing:1px}
.cdur{color:var(--green);font-size:11px;border:1px solid #2b4a3a;border-radius:20px;padding:2px 8px}
.cp{margin-left:auto;background:#1b2130;border:1px solid var(--line);color:var(--txt);border-radius:7px;padding:5px 11px;font-size:12px;cursor:pointer}
.cp:hover{border-color:var(--green);color:var(--green)}
.cp.done{color:var(--green);border-color:var(--green)}
pre.txt{margin:0;padding:15px;white-space:pre-wrap;word-wrap:break-word;font:13.5px/1.7 ui-monospace,Menlo,monospace;color:#dfe5ec}
.men{color:var(--green)}
.falta{color:#e0776f;text-decoration:underline dotted}
</style></head><body>
<header><b>STELLA FUGAZ · PROMPTS DEL GUION</b><span class="m">{{N}} bloques de 20s · {{DUR}}</span></header>
<div class="wrap">
<a class="back" href="../../index.html">← Volver al portal</a>

<div class="ids">
  <h3>UUID de los personajes</h3>
  <p>Pega el UUID de cada uno y <b>todos los prompts se completan solos</b>. Se guardan en este navegador.
     Los que falten salen <span class="falta">marcados en rojo</span> — no me los invento, una id falsa es una referencia rota.</p>
  <div class="grid">{{CAMPOS}}</div>
</div>

{{CUERPO}}
</div>
<script>
const IDS = Object.assign({}, {{IDS}}, JSON.parse(localStorage.getItem('stella_ids')||'{}'));

function resolver(t){
  return t.replace(/§([A-Z0-9]+)§/g, (m,p) => IDS[p] || '');
}
function pintar(){
  document.querySelectorAll('pre.txt').forEach(pre => {
    if(!pre.dataset.src) pre.dataset.src = pre.textContent;
    const t = pre.dataset.src;
    pre.innerHTML = t.replace(/@\[([A-Z0-9]+)\]\(§([A-Z0-9]+)§\)/g, (m,n,p) =>
      IDS[p] ? `<span class="men">@[${n}](${IDS[p]})</span>`
             : `<span class="falta">@[${n}](FALTA-ID)</span>`);
  });
  document.querySelectorAll('.ids input').forEach(i => {
    i.classList.toggle('ok', !!IDS[i.dataset.p]);
  });
}
document.querySelectorAll('.ids input').forEach(inp => {
  inp.addEventListener('input', () => {
    const v = inp.value.trim();
    if(v) IDS[inp.dataset.p] = v; else delete IDS[inp.dataset.p];
    localStorage.setItem('stella_ids', JSON.stringify(IDS));
    pintar();
  });
});
document.querySelectorAll('.cp').forEach(b => {
  b.addEventListener('click', async () => {
    const pre = b.closest('.clip').querySelector('pre.txt');
    const t = resolver(pre.dataset.src || pre.textContent)
                .replace(/@\[([A-Z0-9]+)\]\(\)/g, '@$1');
    try { await navigator.clipboard.writeText(t); } catch(e) {}
    b.textContent = '✓ Copiado'; b.classList.add('done');
    setTimeout(() => { b.textContent = '⧉ Copiar'; b.classList.remove('done'); }, 1400);
  });
});
pintar();
</script>
</body></html>"""


if __name__ == "__main__":
    main()
