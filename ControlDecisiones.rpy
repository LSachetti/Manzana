init python:

    def decisionFinal(pushSanti,dropGabriel):
        if pushSanti < 2 and dropGabriel < 2:
            renpy.jump("decision1")
        elif pushSanti > 1 and dropGabriel > 1:
            renpy.jump("decision4")
        elif pushSanti < 2 and dropGabriel > 1:
            renpy.jump("decision2")
        elif pushSanti > 1 and dropGabriel < 2:
            renpy.jump("decision3")
        else:
            renpy.jump("decision4")

    def pedirNombre():
        Nombre = renpy.input("What about you?")
        Nombre = Nombre.strip()
        if Nombre == "":
            Nombre = "Rene"
        return Nombre

screen botones_habitacion(ProxLabel,x,y,imagen):

    imagebutton:
        idle Solid("#00000000")
        hover imagen
        pos (x, y)
        #xsize 200
        #ysize 200
        action Jump(ProxLabel)
        
screen charla_personajes(charla1, charla2,cant,imagen1,x,y, imagen2,x2,y2):
    imagebutton:
        idle imagen1
        hover imagen1
        pos (x,y)
        action Jump(charla1)
    if cant == 2:
        imagebutton:
            idle imagen2
            hover imagen2
            pos (x2,y2)
            action Jump(charla2)

label dropGabriel1:
    $ dropGabriel += 1
    MainC "Being prepared is definitely better than jumping in on impulse."
    MainC "If we'd done what you did back there all three of us would be wounded at best."
    MainC "{i}That{/i} would've slowed us down."
    Jock "..."
    Emo "..."
    Jock "I guess that's true."
    Jock "Thanks for helping me out, little bro."
    Emo "...It's fine, I don't mind."
    "Santiago mumbled and brushed it away, but he avoided his brother's eyes."
    "But he offered Gabriel his shoulder anyway."



    jump contEvent1


label pushSanti1:
    $ pushSanti += 1
    MainC "Being prepared is definitely better than jumping in on impulse."
    MainC "You need to be more confident, Santiago."
    MainC "We wouldn't be in this mess if we'd thought things through with a level head."
    "And I didn't just mean this time."
    "Even the fight with the girls had only happened because of Gabriel's temper."
    #[rare Santiago sonriendo sprite]
    Emo "Yes, exactly."
    Emo "It's always better to think things through."
    Jock "..."
    "Gabriel seemed to be thinking about this too, because he looked absolutely livid."
    "Whether at himself, at me for calling him out, or at Santiago for whatever reason, I didn't know."
    "But he still accepted Santiago's shoulder when he offered it."

    jump contEvent1



