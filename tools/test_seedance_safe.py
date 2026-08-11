#!/usr/bin/env python3
"""Pruebas del transformador. Cada caso es una trampa real del corpus."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seedance_safe import transformar, transformar_html, poner_arrobas

fallos = []

def check(nombre, obtenido, debe_contener=(), no_debe_contener=()):
    for x in debe_contener:
        if x not in obtenido:
            fallos.append(f"{nombre}: FALTA {x!r}\n      en: {obtenido!r}")
    for x in no_debe_contener:
        if x in obtenido:
            fallos.append(f"{nombre}: NO DEBIA APARECER {x!r}\n      en: {obtenido!r}")

# --- 1. el titulo NO puede llevar @ -----------------------------------------
check("titulo mayuscula", poner_arrobas("Title rises: **STELLA FUGAZ**."),
      debe_contener=["STELLA FUGAZ"], no_debe_contener=["@STELLA FUGAZ"])
check("titulo capitalizado", poner_arrobas('the film "Stella Fugaz" opens'),
      debe_contener=["Stella Fugaz"], no_debe_contener=["@Stella Fugaz"])
check("nombre de archivo", poner_arrobas('href="STELLA_FUGAZ.html"'),
      debe_contener=["STELLA_FUGAZ.html"], no_debe_contener=["@STELLA_FUGAZ"])

# --- 2. los @menciones existentes no se duplican ----------------------------
check("mencion existente", poner_arrobas("@StellaArmadura lunges as @VeraArmadura falls"),
      debe_contener=["@StellaArmadura", "@VeraArmadura"],
      no_debe_contener=["@@", "@Stella@"])
check("nombre suelto si recibe @", poner_arrobas("cut to Stella's cry; Vera is down"),
      debe_contener=["@Stella's", "@Vera"])
check("SelkaBebe intacto", poner_arrobas("@SelkaBebe pressed between them"),
      debe_contener=["@SelkaBebe"], no_debe_contener=["@@", "@Selka@"])

# --- 3. el bloque de estilo pierde las marcas -------------------------------
est = transformar("- **Style:** Satoshi Kon–style anime, cinematic composition, "
                  "cinematic mood, 2D hand-painted Ghibli touch, fluid motion.")
check("estilo sin IP", est,
      debe_contener=["hand-painted 2D anime", "painterly watercolor"],
      no_debe_contener=["Ghibli", "Satoshi Kon"])

# --- 4. la linea Negative pierde los tokens prohibidos ----------------------
neg = transformar("- **Negative:** no blood, no gore, no guns, no on-screen text, no watermark.")
check("negative limpio", neg,
      debe_contener=["no on-screen text", "no watermark"],
      no_debe_contener=["blood", "gore", "guns"])

neg2 = transformar("- **Negative:** no blood, no gore, no guns, no firearms, no on-screen text, no watermark.")
check("negative con firearms", neg2,
      no_debe_contener=["blood", "gore", "guns", "firearms"])

# --- 5. las notas de seguridad del autor ------------------------------------
nota = transformar("**Death shown as her vital glow extinguishing — no blood, no wound.**")
check("nota de la muerte de Vera", nota,
      debe_contener=["glow going out"], no_debe_contener=["blood", "wound"])

nota2 = transformar("drops @Naio with a single pulse of energy (no blood, no wound); "
                    "@StellaArmadura lunges with a scream")
check("nota inline", nota2,
      no_debe_contener=["blood", "wound", "scream"])

# --- 6. la metafora benigna NO se toca --------------------------------------
ben = transformar("sheer stone walls streaked with dead mineral veins")
check("metafora dead", ben, debe_contener=["dead mineral veins"])
ben2 = transformar("a cathedral of emptiness, dead and silent")
check("metafora dead 2", ben2, debe_contener=["dead and silent"])
ben3 = transformar("- **Mood:** gut-punch sacrifice.")
check("metafora gut-punch", ben3, debe_contener=["gut-punch"])

# --- 7. cautiverio / mina ---------------------------------------------------
cau = transformar("Fog-drowned mines, columns of shackled slaves, dim lamps in the murk.")
check("mina", cau, no_debe_contener=["slaves", "shackled"])
cau2 = transformar("wide revealing the caged, beaten allies behind him")
check("aliados", cau2, no_debe_contener=["caged"])

# --- 8. dialogo: cambia la palabra, se conserva el sentido ------------------
dia = transformar('- **Dialogue (@Vorthan):** "What are you doing? She\'s dead. Go find Stella."')
check("dialogo Vorthan", dia,
      debe_contener=["She's gone"], no_debe_contener=["She's dead"])

# --- 9. HTML: el CSS y el JS quedan intactos --------------------------------
# El CSS lleva a proposito una clase .blood y el JS una cadena "kill": si la
# proteccion de <style>/<script> se cae, el transformador los reescribe y
# rompe el estilo y el guion de la pagina. Sin esto la prueba no defiende nada.
html = ('<style>.blood{color:red}.scream{margin:0}</style>'
        '<div class="clip" data-s="clip 1 no blood, no gore">'
        '<pre class="raw" hidden>Negative: no blood, no gore, no guns.</pre></div>'
        '<script>var t="kill";document.querySelector(".blood").id="scream"</script>')
out = transformar_html(html)
check("html css intacto", out, debe_contener=["<style>.blood{color:red}.scream{margin:0}</style>"])
check("html js intacto", out, debe_contener=['var t="kill"', '.blood").id="scream"'])
# Se miran SOLO las zonas que viajan a Seedance (el atributo de busqueda y el
# payload del boton copiar). El .blood del CSS debe seguir ahi: es intocable.
import re as _re
_ds = _re.search(r'data-s="([^"]*)"', out).group(1)
_payload = _re.search(r'<pre class="raw" hidden>([\s\S]*?)</pre>', out).group(1)
check("html data-s limpio", _ds, no_debe_contener=["blood", "gore"])
# el payload es lo que copia el boton: NINGUN token prohibido puede sobrevivir,
# ni siquiera al final de la frase sin coma ("...no guns.")
check("html payload limpio", _payload, no_debe_contener=["blood", "gore", "guns", "firearm"])
check("html etiquetas sanas", out, debe_contener=['<pre class="raw" hidden>'])

# --- 9b. la clausula final sin coma tambien debe morir ----------------------
for cola in ["no blood, no gore, no guns.", "no gore, no guns", "no guns.",
             "no blood.", "no firearms."]:
    r = transformar(f"- **Negative:** {cola}")
    check(f"cola {cola!r}", r, no_debe_contener=["blood", "gore", "gun", "firearm"])

# --- 9c. data-txt: el payload REAL del boton copiar en las paginas SB/IMG ---
# Estructura distinta a PROMPTS_TODOS: si no se limpia, la pagina se ve
# correcta pero el boton entrega el prompt viejo y Seedance lo rebota igual.
h3 = ('<div class="clip" data-txt="Style: Satoshi Kon-style anime. '
      'Negative: no blood, no gore, no guns." data-c="a1" data-k="stella">x</div>')
o3 = transformar_html(h3)
_txt = _re.search(r'data-txt="([^"]*)"', o3).group(1)
check("data-txt limpio", _txt,
      no_debe_contener=["Satoshi", "blood", "gore", "guns"])
check("data-txt conserva mayusculas", _txt, debe_contener=["Style:", "Negative:"])
# los identificadores estructurales NO se tocan: el JS los compara literalmente
check("data-c/data-k intactos", o3, debe_contener=['data-c="a1"', 'data-k="stella"'])

# --- 10. no se rompe el marcado de las etiquetas ---------------------------
html2 = '<div class="f"><span class="fl">Style:</span> Satoshi Kon–style anime</div>'
out2 = transformar_html(html2)
check("html tags intactos", out2,
      debe_contener=['<span class="fl">Style:</span>', "hand-painted 2D anime"],
      no_debe_contener=["Satoshi Kon"])

if fallos:
    print(f"❌ {len(fallos)} FALLOS\n")
    for f in fallos:
        print("  " + f)
    sys.exit(1)
print("✅ todas las pruebas pasan")
