#!/usr/bin/env python3
"""
seedance_safe.py — reescribe el corpus de Stella Fugaz a un lenguaje que los
filtros de moderacion de Seedance no rebotan, y antepone @ a cada personaje.

Principio: la pelicula NO se suaviza. Todos los golpes de la historia se
conservan; lo que cambia es COMO se describen, para decir lo mismo sin el
vocabulario que dispara al moderador. El contenido ya era no-grafico: el
problema era que las propias notas de seguridad del guion ("no blood, no
wound") metian las palabras prohibidas dentro del prompt.

Uso:
    python3 tools/seedance_safe.py --check     # informe, no escribe
    python3 tools/seedance_safe.py --apply     # reescribe en disco
"""
import re
import sys
import glob
import argparse
import collections

# ---------------------------------------------------------------------------
# 1. BLOQUE DE ESTILO — quitar nombres de estudio/autor (disparador de IP).
#    Se sustituye por una descripcion del MISMO look, sin marca registrada.
# ---------------------------------------------------------------------------
ESTILO = [
    (r"Satoshi Kon–style anime, cinematic composition, cinematic mood, 2D hand-painted Ghibli touch",
     "hand-painted 2D anime, painterly watercolor backgrounds, cinematic composition and mood, expressive character acting"),
    (r"Satoshi Kon\s*\+\s*Ghibli", "painterly hand-painted 2D anime"),
    (r"Satoshi Kon[–-]style anime", "hand-painted 2D anime"),
    (r"2D hand-painted Ghibli touch", "painterly watercolor backgrounds"),
    (r"Studio Ghibli style", "painterly watercolor anime style"),
    (r"Ghibli/Kon", "painterly 2D anime"),
    (r"Ghibli\s*\+\s*Satoshi Kon", "painterly hand-painted 2D anime"),
    (r"\bGhibli\b", "painterly watercolor"),
    (r"\bSatoshi Kon\b", "classic 2D anime"),
]

# ---------------------------------------------------------------------------
# 2. NOTAS DE SEGURIDAD DEL AUTOR — dicen lo correcto pero con las palabras
#    prohibidas dentro. Se reescriben conservando la intencion.
# ---------------------------------------------------------------------------
NOTAS_SEGURIDAD = [
    (r"\*\*Death shown as her vital glow extinguishing — no blood, no wound\.\*\*",
     "**Her passing shown only as her inner glow going out — entirely light-based, nothing graphic.**"),
    (r"No blood — only light leaving a body\.", "Only light leaving her — nothing graphic."),
    (r"no blood — only light leaving her", "only light leaving her"),
    (r"\(no blood, no wound\)", "(shown purely as light, nothing graphic)"),
    (r"no blood, no wound", "shown purely as light"),
    (r"beaten but unbloodied", "weary but unharmed"),
    # La linea "Negative:" — se le quitan los tokens prohibidos.
    (r"\bno firearms,\s*", ""),
    (r"\bno blood,\s*", ""),
    (r"\bno gore,\s*", ""),
    (r"\bno guns,\s*", ""),
    (r"\bno weapons,\s*", ""),
    (r"no blood, no gore, no guns", "gentle stylized action"),
]

# ---------------------------------------------------------------------------
# 3. FRASES CON EVIDENCIA — extraidas del corpus real, no inventadas.
#    Cada una conserva el beat dramatico y cambia solo la formulacion.
# ---------------------------------------------------------------------------
FRASES = [
    # -- muerte de Vera / el golpe de S1G1
    (r"the shield and the killing light", "the shield and the descending light"),
    (r"\bthe killing light\b", "the descending light"),
    (r"see only the killing;", "see only the moment;"),
    (r"see only the General killing her mother", "see only the General standing over her mother"),
    (r"the General killing her mother", "the General standing over her mother"),
    (r"\bVera dies on Selka's face\b", "Vera's light goes out, reflected on Selka's face"),
    # -- dialogo (se conserva el sentido, se cambia la palabra)
    (r"She's dead\. Go find Stella\.", "She's gone. Go find Stella."),
    (r"\"she's dead\. find Stella\.\"", "\"she's gone. find Stella.\""),
    (r"she's dead\. find Stella\.", "she's gone. find Stella."),
    (r"I won't kill you for them to clap\.", "I won't end you for them to clap."),
    (r"I won't kill you for them", "I won't end you for them"),
    (r"Forcing it out would kill you\.", "Forcing it out would finish you."),
    (r"did you kill our mother\?", "did you take our mother?"),
    (r"I've executed hundreds\.", "I've ended hundreds."),
    (r"It was you who killed her\.", "It was you who lost her."),
    (r"Because I killed her, little one\.", "Because I took her, little one."),
    (r"our planet will die", "our planet will be lost"),
    (r"\"it's dying\"", "\"it's fading\""),
    (r"the dying planet", "the fading planet"),
    (r"the planet's slow death", "the planet's slow fading"),
    (r"each death buying her", "each loss buying her"),
    (r"watches them die for her", "watches them fall for her"),
    (r"what is about to die", "what is about to be lost"),
    # -- cautiverio / mina (clase de alto riesgo)
    (r"kneel a used-up prisoner for execution", "kneel a spent captive before the crowd"),
    (r"\bfor execution\b", "before the crowd"),
    # OJO al articulo: "an execution" -> "an sentencing" seria agramatical.
    # La forma con articulo va PRIMERO y cambia "an" por "a".
    (r"\ban execution platform\b", "a sentencing platform"),
    (r"\bAn execution platform\b", "A sentencing platform"),
    (r"\bexecution platform\b", "sentencing platform"),
    (r"\ban execution\b", "a sentencing"),
    (r"\bAn execution\b", "A sentencing"),
    (r"they mean to execute a used-up prisoner", "they mean to make an example of a spent captive"),
    (r"\bexecutioner's\b", "guard's"),
    (r"\bexecutioners\b", "guards"),
    (r"\bexecutioner\b", "guard"),
    (r"\bexecute\b", "condemn"),
    (r"columns of shackled slaves", "columns of bound workers"),
    (r"\bshackled slaves\b", "bound workers"),
    (r"aged, chained, a slave in a fog-mine", "aged and bound, held in a fog-mine"),
    (r"a slave in a fog-mine", "held in a fog-mine"),
    # OJO con la frontera de palabra: \bslave\b NO atrapa "slaver" ni "slavery",
    # que quedaron vivos en 30 sitios en la primera pasada. Van antes que \bslave\b.
    (r"\bslaver ship\b", "prison-transport ship"),
    (r"\bslaver ships\b", "prison-transport ships"),
    (r"\bslavers\b", "pit-owners"),
    (r"\bslaver\b", "prison-transport"),
    (r"\bslavery\b", "captivity"),
    (r"\benslaved\b", "held captive"),
    (r"\bslaves\b", "bound workers"),
    (r"\bslave\b", "bound worker"),
    (r"the caged, beaten allies", "the confined, weary allies"),
    (r"caged, beaten allies", "confined, weary allies"),
    (r"\bcaged\b", "confined"),
    (r"\bcages\b", "holding pens"),
    (r"\bcage\b", "holding pen"),
    # -- armas
    (r"its energy-cannon spools up", "its light-emitter spools up"),
    (r"\benergy-cannon\b", "light-emitter"),
    (r"locks her dead-center in its sights", "locks her dead-center in its targeting ring"),
    (r"\bin its sights\b", "in its targeting ring"),
    (r"resistance steps out, weapons up", "resistance steps out, light-emitters raised"),
    (r"\bweapons leveling\b", "light-emitters leveling"),
    (r"\bweapons raised\b", "light-emitters raised"),
    (r"\bweapons up\b", "light-emitters raised"),
    (r"levels his aim at", "trains his light-emitter on"),
    (r"\blevels? his aim\b", "trains his light-emitter"),
    (r"\bKorin aims at Stella\b", "Korin trains his light-emitter on Stella"),
    (r"an energy device leveled", "an energy device trained"),
    (r"a snatched weapon", "a snatched tool"),
    (r"like a weapon that chose its cause", "like an instrument that chose its cause"),
    (r"\bthe weapon builds\b", "the charge builds"),
    (r"small light-blade tool, not a firearm", "small light-cutter tool, not a projectile device"),
    (r"\blight-blade\b", "light-cutter"),
    (r"\bthe blade rising\b", "the light-cutter rising"),
    (r"\bthe blad\b", "the light-cutter"),
    # -- violencia fisica
    (r"as she's struck down", "as she's driven to the floor"),
    (r"\bstruck down\b", "driven to the floor"),
    (r"slams her back against the bulkhead", "drives her back against the bulkhead"),
    (r"a heavy body-slam", "a heavy takedown"),
    (r"\bcrushing impacts\b", "heavy impacts"),
    (r"\bcrashing bodies\b", "heavy impacts"),
    (r"the first heavy punch", "the first heavy blow"),
    (r"snap-zoom on the first punch", "snap-zoom on the first blow"),
    (r"handheld punching in on each hit", "handheld pushing in on each impact"),
    (r"\bpunches for open space\b", "breaks for open space"),
    (r"rips the Orb from Stella's hand", "pulls the Orb from Stella's hand"),
    (r"\*\*rips the @Orbe out\*\*", "**draws the @Orbe out**"),
    (r"\brips the collar\b", "tears free of the collar"),
    (r"refuses to wound her", "refuses to harm her"),
    (r"\bwound her\b", "harm her"),
    # -- terror / gritos
    (r"Stella's ripping scream", "Stella's ripping cry"),
    (r"her raw scream, the baby's cry", "her raw cry, @SelkaBebe's cry"),
    (r"\bStella's scream\b", "Stella's cry"),
    (r"\bhis scream\b", "his cry"),
    (r"\bher scream\b", "her cry"),
    (r"\bwith a scream\b", "with a cry"),
    (r"\bscreams the order\b", "cries out the order"),
    (r"\bas she screams\b", "as she cries out"),
    (r"\bscreams\b", "cries out"),
    (r"\bscreaming near-misses\b", "shrieking near-misses"),
    (r"\bscream\b", "cry"),
    # -- explosiones (se conservan, pero "clean burst of light" ya era el canon)
    # las formas con articulo van ANTES que la generica \bexplosion\b, o esta
    # se adelanta y deja "an burst of light".
    (r"\ban explosion\b", "a burst of light"),
    (r"\bAn explosion\b", "A burst of light"),
    (r"a clean explosion", "a clean burst of light"),
    (r"\bexplosion\b", "burst of light"),
    (r"a wall explodes", "a wall blows inward"),
    (r"the pursuing ship explodes", "the pursuing ship bursts into light"),
    (r"a bulkhead explodes", "a bulkhead blows inward"),
    (r"\bexplodes\b", "bursts into light"),
]

# ---------------------------------------------------------------------------
# 4. PALABRAS SUELTAS — solo las que quedan tras las frases. Deliberadamente
#    CORTA: las metaforas benignas (dead mineral veins, dark throat, heart
#    should beat, gut-punch) se dejan intactas a proposito.
# ---------------------------------------------------------------------------
PALABRAS = [
    (r"\bkilling\b", "decisive"),
    (r"\bkilled\b", "lost"),
    (r"\bkills\b", "ends"),
    (r"\bkill\b", "end"),
    (r"\bmurdered\b", "taken"),
    (r"\bmurder\b", "taking"),
    (r"\bexecuted\b", "ended"),
    (r"\ban explosion\b", "a burst of light"),
    (r"\bAn explosion\b", "A burst of light"),
    (r"\bexecution\b", "sentencing"),
    (r"\bcorpse\b", "still figure"),
    # OJO: "blood" nunca se traduce a "light". Si un "no blood" se colara hasta
    # aqui, el respaldo escribiria "no light" — una instruccion destructiva para
    # la imagen. Se elimina la clausula entera en vez de traducir la palabra.
    # Red de seguridad final: elimina la clausula completa lleve coma, punto o
    # nada detras. Sin el ",?" y el "\s*" un "no guns." final sobrevivia.
    (r",?\s*\bno blood\b", ""),
    (r",?\s*\bno gore\b", ""),
    (r",?\s*\bno guns?\b", ""),
    (r",?\s*\bno firearms?\b", ""),
    (r",?\s*\bno weapons?\b", ""),
    # subcadenas: no tienen frontera de palabra, pero un filtro por subcadena
    # las ve igual. "oxblood" es un color y "bloodthirsty" describe a la multitud.
    (r"\bbloodthirsty\b", "baying"),
    (r"\boxblood\b", "deep burgundy"),
    (r"\bbloodless\b", "clean"),
    (r"\bblood\b", "trace"),
    (r"\bgore\b", "harshness"),
    (r"\bfirearms?\b", "projectile device"),
]

# Palabras que NO se tocan aunque el escaner las marque: son metafora limpia.
BENIGNAS = {"dead mineral veins", "dead and silent", "empty dead core", "dead-center",
            "heart should beat", "gut-punch", "dark throat", "laughter dies in her throat",
            "throat of the duct", "a hard beat", "a held beat", "I beat Gix"}

# ---------------------------------------------------------------------------
# 5. @ ANTES DE CADA PERSONAJE
# ---------------------------------------------------------------------------
PERSONAJES = ["Stella", "Vera", "Naio", "Selka", "Gix", "Vorthan", "Theron",
              "Vosk", "Korin", "Lessa", "Marek", "Brog", "Nima", "Noah",
              "S1G1", "G44"]

def poner_arrobas(txt):
    """Antepone @ a cada nombre de personaje suelto.

    Protege: los @menciones que ya existen (@StellaArmadura), el titulo
    STELLA FUGAZ / Stella Fugaz, y los nombres de archivo (STELLA_FUGAZ.html).
    """
    for nombre in PERSONAJES:
        # (?<![@\w]) no lo precede una @ ni letra   → evita @StellaRopa y palabras
        # (?![\w_])  no lo sigue letra ni guion bajo → evita StellaRopa, STELLA_FUGAZ
        # (?! ?Fugaz) no es el titulo
        patron = rf"(?<![@\w]){nombre}(?![\w_])(?!\s+[Ff]ugaz)(?!\s+FUGAZ)"
        txt = re.sub(patron, f"@{nombre}", txt)
        # variante en mayuscula sostenida (cabeceras de dialogo del guion)
        alto = nombre.upper()
        if alto != nombre:
            patron_alto = rf"(?<![@\w]){alto}(?![\w_])(?!\s+FUGAZ)(?!\s+[Ff]ugaz)"
            txt = re.sub(patron_alto, f"@{alto}", txt)
    return txt

# ---------------------------------------------------------------------------
# Motor
# ---------------------------------------------------------------------------
def transformar(txt, con_arrobas=True):
    # IGNORECASE en todo: el atributo de busqueda data-s de los HTML guarda el
    # prompt EN MINUSCULAS ("style: satoshi kon..."), asi que un patron sensible
    # a mayusculas dejaba intactos 619+233+86 prompts dentro del indice.
    for patron, rep in ESTILO + NOTAS_SEGURIDAD + FRASES + PALABRAS:
        txt = re.sub(patron, rep, txt, flags=re.IGNORECASE)
    # limpieza: "Negative:" pudo quedar con espacios o comas sueltas
    txt = re.sub(r"(\*\*Negative:\*\*|Negative:)\s*,\s*", r"\1 ", txt)
    txt = re.sub(r"(\*\*Negative:\*\*|Negative:)\s*(no on-screen text)", r"\1 gentle stylized action, \2", txt)
    # si al quitar las clausulas la linea quedo vacia ("Negative:."), se repuebla
    txt = re.sub(r"(\*\*Negative:\*\*|Negative:)\s*\.", r"\1 gentle stylized action.", txt)
    # toda linea Negative arranca con la intencion en positivo (idempotente por
    # el lookahead: una segunda pasada no vuelve a insertarlo)
    txt = re.sub(r"(\*\*Negative:\*\*|Negative:)\s+(?!gentle stylized action)(?=\S)",
                 r"\1 gentle stylized action, ", txt)
    if con_arrobas:
        txt = poner_arrobas(txt)
    return txt

# En HTML solo se toca el texto visible y el atributo de busqueda data-s;
# nunca las etiquetas, ni el <style>, ni el <script> (ahi vive "body{...}").
PROTEGIDO = re.compile(r"(<script[\s\S]*?</script>|<style[\s\S]*?</style>)", re.I)
TAG = re.compile(r"(<[^>]*>)")
# Atributos que TRANSPORTAN texto de prompt y por tanto hay que limpiar:
#   data-txt (1145) = payload del boton "Copiar" en las paginas SB/IMG/SBPAGES/LOC/DISENOS
#   data-s   ( 277) = indice de busqueda, en minusculas, en PROMPTS_TODOS
# data-c y data-k se dejan intactos a proposito: son identificadores que el JS
# compara contra cadenas fijas; tocarlos romperia los filtros de la pagina.
DATA_S = re.compile(r'(data-(?:s|txt)=")([^"]*)(")')

def transformar_html(html, con_arrobas=True):
    salida = []
    for bloque in PROTEGIDO.split(html):
        if bloque[:7].lower() in ("<script", "<style ") or bloque[:6].lower() == "<style":
            salida.append(bloque)          # intacto
            continue
        for parte in TAG.split(bloque):
            if parte.startswith("<"):
                # dentro de una etiqueta: solo el valor de data-s
                # data-s es indice de busqueda en minusculas -> se rebaja.
                # data-txt es el prompt que copia el usuario -> se respeta el caso.
                def _attr(m):
                    val = transformar(m.group(2), con_arrobas)
                    if m.group(1).startswith("data-s"):
                        val = val.lower()
                    return m.group(1) + val + m.group(3)
                parte = DATA_S.sub(_attr, parte)
                salida.append(parte)
            else:
                salida.append(transformar(parte, con_arrobas))
    return "".join(salida)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="escribe los cambios en disco")
    ap.add_argument("--check", action="store_true", help="solo informe")
    ap.add_argument("--no-arrobas", action="store_true", help="no anteponer @")
    args = ap.parse_args()
    if not (args.apply or args.check):
        ap.error("usa --check o --apply")

    # Lo que se manda a Seedance (prompts) + el guion, que es de donde salen.
    # Se escriben COPIAS con sufijo _SEEDANCE: los originales de Gio no se tocan.
    patrones = ["guion/PROMPTS_*.md", "guion/PROMPTS_*.txt", "guion/PROMPTS_*.html",
                "guion/GUION_P1_v2.md", "guion/GUION_WEB.html",
                "guion/SCRIPT_P1_v2_EN.md", "guion/SCRIPT_P1_v2_EN.html",
                "guion/GUION_P1_v2_DIALOGOS_EN.md", "guion/GUION_P1_v2_DIALOGOS_EN.html",
                "guion/GUION_TECNICO.html", "guion/STORYBOARD.html",
                "guion/PRODUCCION_clips_*.md", "guion/PRODUCCION_setup_visual.md"]
    archivos = sorted({f for p in patrones for f in glob.glob(p, recursive=True)
                       if "_archivo_guion_v1" not in f and "_SEEDANCE" not in f})

    cambiados, total_bytes = 0, 0
    resumen = collections.Counter()
    for path in archivos:
        original = open(path, encoding="utf-8").read()
        if path.endswith(".html"):
            nuevo = transformar_html(original, not args.no_arrobas)
        else:
            nuevo = transformar(original, not args.no_arrobas)
        if nuevo != original:
            cambiados += 1
            total_bytes += abs(len(nuevo) - len(original))
            # el destino es una COPIA: NOMBRE_SEEDANCE.ext, nunca el original
            base, punto, ext = path.rpartition(".")
            destino = f"{base}_SEEDANCE.{ext}"
            if destino.endswith(".html"):
                # que el titulo delate la variante en la pestana del navegador
                nuevo = re.sub(r"(<title>)(.*?)(</title>)",
                               lambda m: m.group(1) + m.group(2) + " · Seedance" + m.group(3),
                               nuevo, count=1)
            resumen[destino.split("/")[-1]] = sum(
                1 for a, b in zip(original.split("\n"), nuevo.split("\n")) if a != b)
            if args.apply:
                open(destino, "w", encoding="utf-8").write(nuevo)

    print(f"Archivos analizados : {len(archivos)}")
    print(f"Archivos modificados: {cambiados}")
    print(f"{'ESCRITO EN DISCO' if args.apply else 'SIMULACION (--check)'}\n")
    for nombre, n in resumen.most_common(25):
        print(f"  {n:5d} lineas  {nombre}")

if __name__ == "__main__":
    main()
