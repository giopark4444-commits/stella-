#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la versión ETIQUETADA del guion: los nombres cambiados por los @tags reales.

    guion/GUION_P1_v2.md  →  guion/GUION_P1_v2_TAGS.md

El tag de cada personaje **depende de la secuencia** (Stella tiene once estados,
Vera ocho, Selka nueve), así que el mapa de abajo es por SEC. La versión con
nombres normales NO se toca: esta es un archivo aparte.

Uso:  python3 tools/gentags.py
"""
import re, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MD   = RAIZ / "guion" / "GUION_P1_v2.md"
OUT  = RAIZ / "guion" / "GUION_P1_v2_TAGS.md"

# ── quién no cambia nunca ────────────────────────────────────────────────────
FIJOS = {
 "BROGU":"@brogu","NIMA":"@nima","VOSK":"@vosk","GARA":"@gara","ENKO":"@enko",
 "BORO":"@boro","HESSA":"@hessa","YURI":"@yuri","SABO":"@sabo","THARA":"@thara",
 "THERON":"@theron","MAREK":"@marek","KORIN":"@korin-2","LESSA":"@char_lessa",
 "CARL":"@carl","LUCY":"@char_lucy","NOAH":"@char_noah",
 "PRESENTADOR":"@char_junk-planet-fight-host",
 "REY DEL BASURERO":"@junk-king","EL REY DEL BASURERO":"@junk-king",
 "REBELDES":"@rebel-people","S1G1":"@robot-s1g1",
 "ROBOT DEMOLEDOR":"@robot-giant-demoledor","DEMOLEDOR":"@robot-giant-demoledor",
 "VOZ (RADIO)":"@char_erdian-people",
}

# ── quién cambia, por secuencia ──────────────────────────────────────────────
V = {  # SEC : {NOMBRE: tag}
 "2":  {"STELLA":"@stella-cloths","VERA":"@vera-luzagua-park","SELKA":"@selka-baby","GIX":"@gix"},
 "3":  {"STELLA":"@stella-armor","VERA":"@vera-armor","SELKA":"@selka-baby","NAIO":"@naio","VORTHAM":"@vortham"},
 "4":  {"STELLA":"@stella-armor","VERA":"@vera-armor","SELKA":"@selka-baby"},
 "5":  {"STELLA":"@stella-armor-blood","VERA":"@vera-blood","SELKA":"@selka-baby",
        "VORTHAM":"@vortham","GIX":"@gix-giant"},
 "6":  {"STELLA":"@stella-short-hair-armor-blood","VERA":"@vera-more-blood",
        "SELKA":"@selka-baby","VORTHAM":"@vortham"},
 "7":  {"STELLA":"@stella-short-hair-armor-blood"},
 "8":  {"STELLA":"@stella-short-hair-armor-blood"},
 "9":  {"VORTHAM":"@vortham","SELKA":"@selka-baby"},
 "10": {"STELLA":"@stella-short-hair-armor-blood"},
 "10A":{"STELLA":"@stella-short-hair-armor-blood"},
 "11": {"STELLA":"@stella-short-hair-theron"},
 "12": {"VERA":"@char_vera-rebel-hoodie"},
 "12A":{"SELKA":"@selka-girl","VORTHAM":"@vortham-no-coat"},
 "13": {"STELLA":"@stella-short-hair-theron → @stella-collar"},
 "13B":{"STELLA":"@stella-collar"},
 "14": {"STELLA":"@stella-collar"},
 "15": {"STELLA":"@stella-collar","GIX":"@gix-giant"},
 "15B":{"STELLA":"@stella-short-hair-theron"},
 "16": {"STELLA":"@stella-long-hair-theron","GIX":"@gix"},
 "17": {"STELLA":"@stella-long-hair-theron"},
 "18": {"STELLA":"@stella-long-hair-theron","VERA":"@vera-rebel"},
 "19": {"VERA":"@vera-rebel","NAIO":"@naio-prison"},
 "20": {"VERA":"@vera-rebel","SELKA":"@selka-teen"},
 "20A":{"SELKA":"@selka-teen","VERA":"@vera-damaged-1"},
 "20B":{"STELLA":"@char_stella-adult-theron-cloths","GIX":"@gix"},
 "20C":{"STELLA":"@char_stella-adult-theron-cloths","GIX":"@gix"},
 "20D":{"STELLA":"@stella-therons-armor"},
 "21": {"STELLA":"@char_stella-adult-armor"},
 "22": {"STELLA":"@char_stella-adult-armor"},
 "23": {"STELLA":"@char_stella-adult-armor","NAIO":"@naio-prison-2"},
 "23B":{"STELLA":"@char_stella-adult-armor"},
 "24": {"STELLA":"@char_stella-adult-armor","SELKA":"@selka-adult-ver-1","VORTHAM":"@vortham"},
 "25": {"STELLA":"@char_stella-adult-armor","SELKA":"@selka-adult-ver-1","VORTHAM":"@vortham"},
 "26": {"STELLA":"@char_stella-adult-armor","SELKA":"@selka-adult-ver-1",
        "VORTHAM":"@vortham-transformation","VERA":"@vera-rebel"},
 "27": {"STELLA":"@char_stella-adult-armor","SELKA":"@selka-no-arm-ver-1",
        "VORTHAM":"@vortham-parasite","GIX":"@gix-giant"},
 "28": {"VORTHAM":"@vortham-parasite"},
 "29A":{"SELKA":"@selka-no-arm-ver-1 → @selka-ending-1"},
 "29B":{"STELLA":"⚠️@stella-tanque-FALTA","SELKA":"@selka-ending-1","NAIO":"@naio-prison-2"},
}

def rep_factory(mapa):
    def rep(mm):
        nom = mm.group(1).strip()
        tag = mapa.get(nom)
        if not tag: return mm.group(0)
        cont = (mm.group(2) or "") + (mm.group(3) or "")
        return f"**{tag}{cont}**"
    return rep

LOC = {
 "0":"@loc_erdia-square-destroyed · @loc_facade · @loc_duct","1":"@loc_erdia-past",
 "2":"@loc_luzagua-park","3":"@loc_erdia-palace-lab","4":"@erdia-palace-corridors",
 "5":"@loc_erdia-orbe-room","6":"@loc_erdia-orbe-room-destroyed · @loc_duct",
 "7":"@loc_erdia-past","8":"⚠️ interior de la nave — FALTA · @ship-stella",
 "9":"⚠️ balcón real — FALTA","10":"@loc_modershipo-hospital","10A":"@loc_modershipo-hospital",
 "11":"⚠️ pasillos de la Nodriza — FALTA · @loc_nimas-laboratory",
 "12":"@loc_rebel-house","12A":"@loc_erdia-palace-traingin-room",
 "13":"@loc_junk-planet","13B":"@loc_junk-planet-market","14":"@loc_junk-planet-colisseum",
 "15":"@loc_junk-planet-colisseum","15B":"@loc_nimas-laboratory",
 "16":"⚠️ planeta de los cometas — FALTA · @loc_nimas-laboratory",
 "17":"@mothership-control-room","18":"⚠️ camarote — FALTA",
 "19":"@loc_prison-corridor · @loc_prison-cell","20":"@selkas-dorm","20A":"@selkas-dorm",
 "20B":"⚠️ 3–4 mundos — FALTAN · @loc_mothership-bar · @loc_mothership-hall",
 "20C":"@space-port · @loc_space-port-lake · @loc_space-port-view",
 "20D":"@loc_nimas-laboratory","21":"@loc_erdia-dry · @loc_erdia-destroyed",
 "22":"@loc_rebel-house","23":"@loc_prison-corridor · @loc_prison-cell",
 "23B":"@loc_erdia-square-destroyed · @loc_facade","24":"@loc_duct · @loc_erdia-orbe-room",
 "25":"@loc_erdia-orbe-room","26":"@loc_erdia-orbe-room","27":"@loc_erdia-orbe-room",
 "28":"@loc_erdia-future-sky · @loc_erdia-square-destroyed",
 "29A":"@loc_modershipo-hospital","29B":"@loc_mothership-recovery-room",
}

def reparto(txt, mapa):
    """Quién está DE VERDAD puesto en escena aquí.

    Cuenta si aparece marcado en negrita (**NOMBRE**) —que es como el guion pone a
    alguien en el plano— o si el nombre en capitalizado sale **dos veces o más**.
    Una sola mención suelta en una acotación NO cuenta: si no, Marek acabaría en el
    reparto de la sala del Orbe por una frase que habla de él.
    """
    vistos, ya = [], set()
    for nom, tag in mapa.items():
        if tag in ya: continue
        negrita = re.search(r"\*\*[\"“]?" + re.escape(nom) + r"[\"”]?[ (.,:;]", txt) or f"**{nom}**" in txt
        veces = len(re.findall(r"\b" + re.escape(nom.title()) + r"\b", txt))
        if negrita or veces >= 2:
            vistos.append((nom, tag)); ya.add(tag)
    return vistos

md = MD.read_text(encoding="utf-8")
cabecera, cuerpo = md[:md.index("# ACTO")], md[md.index("# ACTO"):]
NOM = re.compile(r"\*\*[\"“]?([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ0-9 ]{1,24})[\"”]?( \(CONT\.\))?([.,:;]?)\*\*")

PROPS = {
 "3":"@prop_orbe-locker *(la caja de la mano)* · @prop_stella-armor-ver-1-1 · @prop_stella-bracelet",
 "5":"@prop_orbe-in-room · @prop_orb · @prop_stella-bracelet · ⚠️ escudo de Vera — FALTA · ⚠️ muñequera — FALTA",
 "4":"⚠️ escudo de Vera — FALTA · @prop_stella-bracelet",
 "6":"⚠️ muñequera — FALTA · @prop_stella-bracelet",
 "7":"@ship-stella · @ship-enemy-erdia · @ship-4-enemyy · @ship-erdia-1",
 "8":"@ship-stella · @prop_orb","9":"@ship-enemy-erdia",
 "10":"@prop_orb · @prop_stella-bracelet","10A":"@prop_stella-bracelet",
 "13":"@prop_collar · @prop_junk-king-orb *(el amuleto)*",
 "13B":"@prop_collar","14":"@prop_collar · @prop_junk-king-orb *(el amuleto)*",
 "15":"@prop_collar · @prop_junk-king-orb *(el amuleto)* · ⚠️ 3 cristales de Nima — FALTAN · @mothership",
 "16":"⚠️ espada, lanza y arco — FALTAN · @prop_stella-armor-ver-1-1",
 "18":"⚠️ proyector de Vera — FALTA",
 "20B":"⚠️ mapa del salón — FALTA · ⚠️ proyector — FALTA · ⚠️ 3 cristales — FALTAN",
 "20D":"@prop_stella-bracelet · @stella-therons-armor",
 "23B":"@prop_palace-cover *(la placa soldada)*","0":"@prop_palace-cover *(la placa soldada)*",
 "29A":"@selka-ending-1 *(el brazo nuevo)* · ⚠️ 3 cristales de Nima — FALTAN","29B":"@selka-ending-1",
 "24":"@prop_orb · @prop_stella-bracelet","25":"@prop_orb · @prop_orbe-in-room",
 "27":"@prop_orb · @prop_stella-bracelet","28":"@mothership",
}

# trocear por secuencia para poder mirar el texto entero de cada una
trozos = re.split(r"(?m)^(## SEC\. [0-9]+[A-D]? .*)$", cuerpo)
fuera, mapa = [], dict(FIJOS)
i = 0
while i < len(trozos):
    if trozos[i].startswith("## SEC."):
        cab_sec, texto = trozos[i], trozos[i+1] if i+1 < len(trozos) else ""
        sec = re.match(r"## SEC\. ([0-9]+[A-D]?) ", cab_sec).group(1)
        mapa = dict(FIJOS); mapa.update(V.get(sec, {}))
        cast = reparto(texto, mapa)
        # si le declaré un estado a alguien en esta SEC, está en la escena aunque
        # el texto solo lo nombre una vez (Selka en brazos, p.ej.)
        ya = {tg for _, tg in cast}
        for nm, tg in V.get(sec, {}).items():
            if tg not in ya: cast.append((nm, tg)); ya.add(tg)
        fuera.append(cab_sec); fuera.append("")
        fuera.append(f"> 🏷️ **LOCACIÓN** · `{LOC.get(sec,'—')}`")
        if cast:
            fuera.append("> 🏷️ **REPARTO** · " + " · ".join(f"`{v}`" for _, v in cast))
        if sec in PROPS:
            fuera.append(f"> 🏷️ **PROPS** · `{PROPS[sec]}`")
        for linea in texto.splitlines():
            fuera.append(NOM.sub(rep_factory(mapa), linea))
        i += 2; continue
    for linea in trozos[i].splitlines():
        fuera.append(NOM.sub(rep_factory(dict(FIJOS)), linea))
    i += 1


CAB = """# STELLA · *a falling star* — **VERSIÓN ETIQUETADA**
## Guion — Película 1 (v2.7) · **nombres sustituidos por los @tags de la biblioteca**

> ⚠️ **Esta versión es para producir prompts, no para leer.** El guion normal, con los nombres,
> está en `GUION_P1_v2.md` y **no se toca**: este se regenera con `python3 tools/gentags.py`.
>
> **Cómo funciona:** el tag de cada personaje **cambia según la secuencia** — Stella tiene once
> estados, Vera ocho, Selka nueve. Cada `## SEC` empieza con dos líneas 🏷️ que dicen **la locación**
> y **qué personajes cambian de tag ahí**. Dentro del texto, los nombres ya vienen sustituidos.
>
> ⚠️ **`⚠️@…-FALTA`** marca un estado que **todavía no existe en la biblioteca.**
> ⚠️ **Los diálogos y las acotaciones NO se etiquetan** — solo la acción y los pies de personaje.

"""
OUT.write_text(CAB + "\n".join(fuera).rstrip() + "\n", encoding="utf-8")
print(f"✓ {OUT.name}  ·  {len(OUT.read_text(encoding='utf-8')):,} bytes")
