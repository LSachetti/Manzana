define ratio = 0.45
define posXder = 0.8
define posYGab = 0.9
define posXizq = 0.3


transform centroDer:
    xalign 0.8
    yalign 1.0

transform centroIzq:
    xalign 0.2
    yalign 1.0

init python in director:    
    # ....
    #define transform tam = zoom 0.5

    transforms = [ "left", "center", "right", "truecenter", "top", "size" ]

    transitions = [ 
        "fade", 
        "dissolve", 
        "pixellate", 
        "move", 
        "move", 
        "moveinright",  
        "moveinleft", 
        "moveintop", 
        "moveinbottom", 
        "moveoutright", 
        "moveoutleft", 
        "moveouttop", 
        "moveoutbottom", 
        "ease", 
        "easeinright", 
        "easeinleft", 
        "easeintop", 
        "easeinbottom", 
        "easeoutright", 
        "easeoutleft", 
        "easeouttop", 
        "easeoutbottom",
        "zoomin",
        "zoomout",
        "zoominout",
        "vpunch",
        "hpunch",
        "blinds",
        "squares",
        "wipeleft",
        "wiperight", 
        "wipeup", 
        "wipedown",
        "slideleft",
        "slideright", 
        "slideup", 
        "slidedown",
        "slideawayleft",
        "slideawayright", 
        "slideawayup", 
        "slideawaydown",
        "pushright",
        "pushleft", 
        "pushup", 
        "pushdown",
        "irisin", 
        "irisout"
        ]
        # ....

#default prn = "Test"
define Nombre = "Rene"
define canal = "PlaceHolder"
define petNemo = "Santi"
define MainC = Character("[Nombre]")
define Emo = Character("Santiago", image = "santiago")
define Jock = Character("Gabriel", image = "gabriel")
define Darks = Character("Abril", image = "abril")
define Pastel = Character("Martina", image = "martina")
define OtroCam = Character("Facundo")


image martina:
    "/Martina sprites/martina.png"
    zoom  0.6
    yalign 1.0
    yoffset 500
image martina triste:
    "/Martina sprites/martina triste.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina asustada:
    "/Martina sprites/martina asustada.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina asustada2:
    "/Martina sprites/martina asustada2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina enojada:
    "/Martina sprites/martina enojada.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina enojada2:
    "/Martina sprites/martina enojada2.png"
    zoom  0.6
    yalign 1.0
    yoffset 500
image martina enojada3:
    "/Martina sprites/martina enojada3.png"
    zoom  0.6
    yalign 1.0
    yoffset 500
image martina feliz:
    "/Martina sprites/martina feliz.png"
    zoom  0.6
    yalign 1.0
    yoffset 500
image martina feliz2:
    "/Martina sprites/martina feliz2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina llorando:
    "/Martina sprites/martina llorando.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina neutral:
    "/Martina sprites/martina neutral.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina sonrisa:
    "/Martina sprites/martina sonrisa.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina sonrisa2:
    "/Martina sprites/martina sonrisa2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina sorprendida:
    "/Martina sprites/martina sorprendida.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina triste2:
    "/Martina sprites/martina triste2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image martina triste3:
    "/Martina sprites/martina triste3.png"
    zoom 0.6
    yalign 1.0
    yoffset 500

image santiago asustado:
    "/Santiago sprites/santiago asustado.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago creepy:
    "/Santiago sprites/santiago creepy.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago creepy2:
    "/Santiago sprites/santiago creepy2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago creepy3:
    "/Santiago sprites/santiago creepy3.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago feliz:
    "/Santiago sprites/santiago feliz.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago lastimado:
    "/Santiago sprites/santiago lastimado.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago llorando:
    "/Santiago sprites/santiago llorando.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago neutral:
    "/Santiago sprites/santiago neutral.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago neutral2:
    "/Santiago sprites/santiago neutral2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago resignado:
    "/Santiago sprites/santiago resignado.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago silly:
    "/Santiago sprites/santiago silly.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago sonrisa:
    "/Santiago sprites/santiago sonrisa.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago sorprendido:
    "/Santiago sprites/santiago sorprendido.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago triste2:
    "/Santiago sprites/santiago triste2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image santiago:
    "/Santiago sprites/santiago.png"
    zoom 0.6
    yalign 1.0
    yoffset 600

image gabriel:
    "/Gabriel sprites/gabriel.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel asustado:
    "/Gabriel sprites/gabriel asustado.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel enojado:
    "/Gabriel sprites/gabriel enojado.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel enojado2:
    "/Gabriel sprites/gabriel enojado2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel enojado3:
    "/Gabriel sprites/gabriel enojado3.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel feliz:
    "/Gabriel sprites/gabriel feliz.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel forzada:
    "/Gabriel sprites/gabriel forzada.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel forzada2:
    "/Gabriel sprites/gabriel forzada2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel neutral:
    "/Gabriel sprites/gabriel neutral.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel sobrador:
    "/Gabriel sprites/gabriel sobrador.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel sonrisa:
    "/Gabriel sprites/gabriel sonrisa.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel sonrisa2:
    "/Gabriel sprites/gabriel sonrisa2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel triste2:
    "/Gabriel sprites/gabriel triste2.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel sorprendido:
    "/Gabriel sprites/gabriel sorprendido.png"
    zoom 0.6
    yalign 1.0
    yoffset 600
image gabriel triste:
    "/Gabriel sprites/gabriel triste.png"
    zoom 0.6
    yalign 1.0
    yoffset 600

image abril:
    "/Abril sprites/abril.png"
    zoom 0.6
    yalign 1.0
    yoffset 500

image abril asustada:
    "/Abril sprites/abril asustada.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril asustada2:
    "/Abril sprites/abril asustada2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril desafiante:
    "/Abril sprites/abril desafiante.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril enojada:
    "/Abril sprites/abril enojada.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril enojada 2:
    "/Abril sprites/abril enojada 2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril exasperada:
    "/Abril sprites/abril exasperada.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril llorando:
    "/Abril sprites/abril llorando.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril ojososcuros:
    "/Abril sprites/abril ojososcuros.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril seria:
    "/Abril sprites/abril seria.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril seria2:
    "/Abril sprites/abril seria2.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril sorprendida:
    "/Abril sprites/abril sorprendida.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
image abril triste:
    "/Abril sprites/abril triste.png"
    zoom 0.6
    yalign 1.0
    yoffset 500
