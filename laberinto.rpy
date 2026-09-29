# ============================================================
# IMÁGENES
# ============================================================

image entrada = "bg entrada"
image manzana = "manzanaTest.jpg"


# ============================================================
# ENTRADA
# ============================================================

screen laberinto_entrada():

    imagebutton:
        idle "images/cuadrado.png"
        xpos 500
        ypos 500

        action Return("puerta")

label Laberinto:

    scene entrada
    call screen laberinto_entrada

    if _return == "puerta":
        jump puerta1


# ============================================================
# PUERTA 1
# ============================================================

label puerta1:

    scene manzana

    "aver"
    "esto es otra escena idk"

    pause
screen cursor_position():

    $ x, y = renpy.get_mouse_pos()

    text "Cursor: [x], [y]":
        xalign 0.5
        yalign 0.05

    timer 0.05 repeat True action Function(renpy.restart_interaction)    