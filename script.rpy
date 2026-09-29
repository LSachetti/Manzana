

define config.default_text_cps = 30      # compatibilidad / valor por defecto del motor
default preferences.text_cps = 60        # forma recomendada: preferencia por defecto







label start:

    scene bg test
    play music ambience_outside volume 2.0

    "The excavators in this particular plot of land had been turned off a few weeks ago."
    "It had been all over the news for a while. \"New tunnels discovered at demolition site!\" the broadcasts read, \"How deep do they go?\" they wondered."
    "So all demolition was halted, the construction company retreating from the potential archeological site, permits for proper investigation were requested, and so on, and so forth."
    "Not that it was all that strange for a network of tunnels to be found in this particular area."
    "In fact, La Manzana de las Luces was not that far, and it's known that there are several other ones running under Buenos Aires, uncharted, some partially damaged, some inaccessible."
    "The known tunnel entrances are usually being watched, tourist traps that they are. You can do guided tours through them."
    "But this tunnel was different."
    "The construction workers had long shrugged their shoulders and left, the investigators hadn't arrived yet, there were no tourists, no tours."
    "Sure, there were a couple of security guards from time to time, but they were mostly watching the machines. Being as dark as it was, it wouldn't be that hard to walk right past them if I stuck to the shadows, or to wait until their shift change."
    "There wouldn't be a more perfect time to sneak in."
    "I was thinking about all this as I stood just outside, my camera on hand."
    "The entrance stood there, a gaping maw where the light went to die."
    #MC
    "{i}The tunnels, how deep do they go?{/i}"
    "..."
    play sound attention_sound volume 0.75 
    "A hand grabbed at my shoulder."
    with hpunch
    "???" "\"Augh?!\""
    "Taken aback, I spun around on my heels."
    "Four people in total stood there, gaping at my reaction."
    "I must've really been zoning out, if a group this big could sneak up on me."

    #[Pastel sad sprite]
    show martina triste with dissolve 
    play sound pastel_aww
    "Pink Hair" "\"Aww, you scared him, Jock.\""

    #[sprite del chabón a la defensiva]
    show martina triste at centroIzq with easeinleft
    show gabriel sonrisa2 at centroDer  with dissolve
    "Jock" "I didn't mean to."
    show gabriel sonrisa
    "Jock" "Excuse me, are you [OtroCam]?"
    "???" "Huh?"
    hide gabriel
    hide martina
    show abril seria2 with dissolve
    "Blue Stripe" "We know [OtroCam], that's not [OtroCam]."
    play sound emo_mmm
    show abril seria2 at centroDer with easeinright
    show santiago neutral2 at centroIzq with dissolve
    "Vampire Guy" "But [OtroCam] has a camera..."
    "I focused on what they were carrying."
    "All four of them had hefty backpacks and a camera of their own. That's when it hit me."
    "???" "Ah, it's you lot. I've been waiting for you."
    MainC "[OtroCam] sent me, actually. He said he couldn't make it."
    show abril triste
    ##"[Darks] sighed."
    play sound darks_sigh
    show abril exasperada
    "Blue Stripe" "Yeah, that tracks."
    show abril exasperada
    "Blue Stripe" "I told you all he'd flake."
    show santiago neutral
    "Vampire Guy" "Did he say what happened...?"
    "I thought about it."
    "???" "Not really, but he sounded like he wasn't super psyched about it."
    "???" "We're filming inside the tunnels, right?"
    play sound pastel_happy_mhm
    hide santiago
    hide abril
    show martina feliz2 at centroIzq with vpunch
    "Pink Hair" "Yeah!"
    show martina sonrisa2 at center with easeinleft
    "Pink Hair" "This place is going to be crawling with people next week."
    show martina feliz2 at centroDer with easeinleft
    "Pink Hair" "So we figure if we want to explore them, it's now or never!"
    show martina feliz at center with vpunch:
        zoom 1.5
        yalign 0.5
    "Pink Hair" "I'm Martina, by the way! And these are..."
    hide martina
    show abril seria with dissolve
    Pastel "Abril," #[mostrar sprite de la Darks]
    hide abril
    show santiago neutral2 with dissolve
    Pastel "Santiago," #[mostrar sprite del Emo]
    hide santiago
    show gabriel sonrisa with dissolve
    Pastel "And Santiago's brother." #[mostrar sprite Jock]
    show gabriel forzada2
    #[Jock irritado pero con una sonrisa]
    play sound jock_scoff
    Jock "It's [Jock], actually."
    hide gabriel
    $ Nombre = pedirNombre() 
    menu:
        "What are your pronouns?"
        "She/Her/Hers":
            $subject = "she"
            $contration = "she's"
            $object1 = "her"
            $possessive = "hers"
            $possessive_adjective = "her"
            $reflexive = "herself"
            #renpy.jump("next_part")
        "He/Him/His":
            $subject = "he"
            $contration = "he's"
            $object1 = "him"
            $possessive = "his"
            $possessive_adjective = "his"
            $reflexive = "himself"
            #renpy.jump(next_part)
        "They/Them/Theirs":
            $subject = "they"
            $contration = "they're"
            $object1 = "them"
            $possessive = "theirs"
            $possessive_adjective = "their"
            $reflexive = "themselves"
            #renpy.jump(next_part)
            #add !c after the string
    MainC "[MainC]. Nice to meet you all."
    MainC "Anyhow, if we're going to go in, you came here at the right time."
    #show abril 
    show abril seria with dissolve
    Darks "Why is that?"
    MainC "Because it's almost dinnertime."
    hide abril
    scene black with fade
    stop music fadeout 1.0
    play sound steps volume 2.0
    pause (2.0)
    play music ambience_tunel fadein 1.0
    screen cursor_position():

        $ x, y = renpy.get_mouse_pos()

        text "Cursor: [x], [y]":
            xalign 0.5
            yalign 0.05

        timer 0.05 repeat True action Function(renpy.restart_interaction)
    
    scene bg test3 with dissolve
    #ESCENA 2
    #jump? label scene2?
    "Sneaking in was even easier than I thought it would be, especially with a group this large."
    "We ran in one by one, waiting to see a flashlight signaling us before sending each and every member of our group."
    with flash
    with vpunch
    "I was the last one in, my eyes struggling to get used to the darkness. And it didn't help when someone flashed their flashlight right into my eyes."
    play sound pastel_whoops
    show martina sorprendida
    Pastel "Woops, sorry!"
    MainC "D-Don't worry about it..."
    show martina sonrisa2
    pause (0.5)
    hide martina with dissolve
    "I tried to be reassuring, knowing that she couldn't see me blinking the tears forming at the corners of my eyes away."
    "That's when I remembered what I was supposed to be doing."
    "I turned my camcorder back on, and though I specifically brought one that was good in low light settings, it was still extremely dark in here, so I turned on my flashlight as well."
    "The walls, made out of something closer to clay than stone, were narrow around us, closing in on us like an unnerving hug."
    "Behind us was the light of the entrance. In front of us, an impenetrable darkness that even our flashlights couldn't cut through."
    "We all stared ahead for a second, until someone broke the silence that had fallen over us."
    play sound darks_grumpy_huh
    show abril seria2 at centroDer
    Darks "Alright, let's go."
    show abril seria
    Darks "If we stay this close to the entrance, sooner or later someone will notice we're in here. We need to go deeper."
    hide abril
    show screen cursor_position

    call screen botones_habitacion("Escena2", 900, 450, "Santiago Sprites/santiago silly.png")


label Escena2:    
    play sound steps volume 2.0
    scene black with fade
    "Making sure everything was in working order, we braved the darkness up ahead."
        #[sfx de pasos con eco, pasan un par de fondos de pasillos distintos]
    "It hadn't been five minutes when a creepy voice from behind me broke the silence."
    centered "{cps=24} Have you heard of the legend, then? {/cps}"
    ##ADD VOICE HERE
    with vpunch
    MainC "?!"
    scene bg test3 with dissolve
    #Review transform
    "I startled so bad I accidentally bumped into Martina."
    play sound pastel_yelp
    show santiago sorprendido at centroIzq with dissolve
    show gabriel feliz at centroDer with dissolve
    Jock "Haha, good one, [Emo]."
    show gabriel sonrisa
    Jock "You scared [MainC] half to death."
    show santiago
    Emo "I was just trying to make conversation..."
    play sound emo_suspiro
    show santiago neutral
    Emo "Sorry about that."
    MainC "It's okay."
        #[más sfx de pasos]
    MainC "I wasn't aware that there was some sort of legend about this place, though. With it being so recent and everything."
    hide gabriel with dissolve
    show santiago neutral
    Emo "Well, it's more like an urban legend that popped up these last few weeks, I guess."
    play sound pastel_giggles
    show martina sonrisa at centroDer with dissolve
    Pastel "A place this creepy has to have something going on!"
    hide martina
    hide santiago
    show abril seria at center with dissolve
    Darks "You're only saying that because it's old."
    show abril seria at centroIzq with easeinleft
    Darks "People will make all sorts of shit up if a place is old enough."
    show santiago neutral2 at centroDer with dissolve
    Emo "Maybe, I don't know."
    show santiago neutral
    Emo "But there've been disappearances around the house that used to be on the entrance even before they found the entrance..."
    Emo "And--"
    show santiago sorprendido with vpunch
    play sound emo_ugh
    Emo "--ugh."
    hide santiago
    hide abril
    "[Darks] stopped walking all of a sudden, causing a chain reaction of collisions."
    play sound pastel_ow
    pause 0.2
    play sound jock_grumpy_scoff
    pause 0.2
    play sound emo_ugh
    show martina enojada2 at centroIzq with dissolve
    Pastel "A little heads up next time would be nice!"
    play sound darks_grumpy_huh
    show abril exasperada at centroDer with dissolve
    Darks "Oh, please."
    hide martina
    hide abril

    scene bg ritual with dissolve
    "The area ahead of us was wider than the narrow tunnels we'd been trudging through, almost like a resting stop."
    "Definitely big enough that we wouldn't have to be staring at each other's backs."
    "[Darks] turned around."
    show abril desafiante with dissolve
    Darks "We can do it here."
    hide abril
    "Everyone but me murmured in agreement."
    MainC "What are we doing, exactly?"
    "The only thing I knew was that they wanted me to record this place."
    show gabriel neutral at centroDer with dissolve
    Jock "Did [OtroCam] not tell you anything?"
    show martina enojada at centroIzq with hpunch
    show gabriel forzada2
    pause (1.0)
    hide gabriel with dissolve
    #play sound jock_grumpy_ugh
    "[Pastel] hit him on the arm."
    show martina feliz2 at center with easeinright
    play sound pastel_giggles
    Pastel "We're making a GoopTube video!"
    show martina feliz
    Pastel "We're into like, you know... cryptids, urban legends, all that sort of supernatural stuff."
    show martina feliz2 at centroIzq with easeinleft
    show abril exasperada at centroDer with dissolve
    play sound darks_grumpy_huh
    Darks "{i}You{/i} are into that sort of supernatural stuff."
    show abril exasperada at center with easeinleft
    show gabriel enojado at centroDer with easeinright
    Jock "All I signed up for was to drive all of you here."
    scene bg ritual
        #[Sprite del emo pero más chiquito que los demás y la voz más bajita]
    play sound emo_mmm
    show santiago silly at center:
        zoom 0.40
        yalign 10
    Emo "{size=*0.75}{cps=24}I think the supernatural is pretty cool...{/cps}{/size}"
    play sound pastel_grumpy_eh
    scene bg ritual with dissolve
    show martina triste with dissolve
    Pastel "You guys are all boring."
    show martina enojada3
    Pastel "Whatever, I'm over it."
    show martina sonrisa
    Pastel "Everyone take positions! We're going to start now!"
    hide abril
    hide santiago
    hide gabriel
    "[Jock] surreptitiously stood behind me as I lifted my camera, still rolling, towards the other three."
    show martina feliz
    Pastel "Aaand... action!"
    show martina feliz2
    Pastel "Welcome to [canal], your weekly fix of the scariest places right here in your vicinity!"
    show santiago creepy at centroDer
    Emo "Today we are exploring the cavernous expanse of a certain tunnel... I'm sure you know which one if you've been looking at the news."
    play sound jock_grumpy_scoff
    "[Jock] scoffed, and not quietly."
    show martina neutral
    "They're going to have to fix that in the edit."
    "I can't blame him for that reaction though. It is creepier that he can switch it up on command..."
    show abril seria at left
    Darks "And if you don't know, you should be paying more attention to the world."
    show abril seria2
    play sound darks_sigh
    Darks "Go watch the news for a change."
    show martina sonrisa2
    play sound pastel_giggles
    Pastel "After you watch the show of course."
    show santiago feliz
    play sound emo_positive_hum
    Emo "Don't forget to leave a like and subscribe!"
    "The three of them stood there smiling (well, two of them were smiling at any rate) for a second too long, like they were waiting for something..."
        #[SFX clapping hands]
    show martina sonrisa
    show abril seria
    show santiago neutral2
    Pastel "Alright, I think that's good for now."
    show abril seria2
    Darks "Not our worst intro."
    show santiago neutral
    Emo "Maybe we could get some b-roll next?"
    scene bg ritual
    "I spent the next few minutes on auto-pilot, pointing my camera at whatever needed to be shot. For such an interesting location, it was quite a mundane affair."
    "Until Martina, who I was quickly realizing ran the ship for the most part, clapped her hands again."
    show martina neutral at centroIzq with dissolve
    Pastel "Alright, we should get on with it then. Did you bring the thing, [petNemo]?"
    hide martina
    "I instinctively pointed my camera at him. He nodded."
    show santiago neutral at centroIzq with dissolve
    play sound emo_positive_hum
    Emo "I stayed up late making it last night..."
    show santiago neutral2
    "Saying this, he produced a strange cloth doll, tied tightly all around its chest with thread."
    "I immediately knew what it was."
    hide santiago
    MainC "Are you guys going to try the ritual?"
    play sound darks_sigh
    show abril seria2 at centroIzq with dissolve
    Darks "Not much else to do down here."
    show abril seria
    Darks "Unless we want to post a video of us walking around in the dark for two hours."
    "I should've known. Every time I go online these days someone is passing that one ritual around, and from what I've heard from them we must move in similar circles."
    "However, I was curious..."
    MainC "You do know about the disappearances, right?"
    play sound jock_damn
    show gabriel enojado at centroDer with dissolve
    Jock "Oh, here we go again."
    show gabriel forzada
    "[Jock] ran a hand through his neat hair with the exasperation that only someone who heard a story a million times and liked it less in every opportunity could have."
    "And judging by [Emo]\'s guilty look, I was pretty sure that was the case."
    show abril desafiante
    play sound darks_grumpy_huh
    Darks "Come on."
    Darks "All those zero-karma accounts who dropped off the internet were clearly trying to drum up hype."
    show santiago at right with dissolve
    play sound emo_suspiro
    Emo "To be fair, from what I researched the disappearances were happening before the first thread was posted..."
    "[Darks], who had been crouching and lighting a candle on the ground rose back to her feet and promptly rolled her eyes."
    show abril exasperada
    play sound darks_sigh
    Darks "There are no supernatural disappearances."
    Darks "People are just retroactively linking the tunnel with random missing people through the years because it makes for a better story."
    show abril desafiante
    play sound darks_grumpy_huh
    Darks "All the more reason to perform this so-called ritual."
    Darks "So that people can see it's not real."
    "Those words reverberated in the empty hollowness of the tunnels."
    "In our silence, all we could hear was the echo of those words, getting farther and farther away."
    "And on everyone else's faces, a question began to form."
    "But what if it is real...?"
    "Gabriel cleared his throat."
    play sound jock_tos
    show gabriel forzada2
    Jock "Can we like, get on it then?"
    Jock "I don't wanna be here all night."
    "He was right."
    "I lifted my camera as Martina grabbed the doll in steady hands, a look of determination on her face."
    "The ritual was about to begin."


        #Escena 3???
    scene bg ritual
    "The whole thing was quite simple."
    "The doll was bound fourteen times with thread."
    "Someone would walk around the candle fourteen times."
    "And every time..."
    play sound creepy_whoosh
    play music horror_music_two volume 2.0
    show martina sonrisa at centroIzq with dissolve
    Pastel "The door stands open."
    "[Pastel] would unravel one loop of thread from the doll, chanting."
    #ADD refe visual?
    Pastel "There is no lock."
    "More thread was stripped off the doll."
    "Another circle."
    show martina neutral
    Pastel "The door stands open."
    Pastel "There is no lock."
    "Little by little, the thread unraveled."
    "The more it happened, the more unease seemed to come over everyone else."
    "But Martina held strong."
    Pastel "The door stands open."
    "It was the eleventh round around the candle."
    "There was a strange lull about us as we stood around her in a circle, entranced by the ceremony of it all."
    Pastel "There is no lock."
    "Even Abril was watching, back straight, her eyebrows furrowed in concentration."
    "Looking like for one second, and one second only..."
    Pastel "The door stands open."
    "...she considered the possibility of not making it back home tonight."
    show martina asustada
    play sound creepy_whoosh
    "[Pastel] stopped in her tracks."
    show martina neutral
    "The thread came off the doll completely."
    "I followed her with my camera as she crouched near the flame, the two ends of the thread in each of her hands. She closed in near the fire..."
    "...and it burned it through, snapping it in two."
    Pastel "Thus we step now over the threshold, O son of kings and queens. May you welcome us in."
    scene black with fade
    stop music fadeout 1.0
    "And she, too, fell into the all-encompassing silence we had been submerged into."
    "It could all have ended there."
    "The quiet overpowering us for one final moment as the video ended."
    "You couldn't ask for much more material for ghost hunting-type viral videos unless you were thinking of faking evidence."
    "But-"
    play music shaking_rocks volume 0.5
    "At that precise moment, the rumbling began."
    #ADD temboleres? flashes?
    "Not of a monster, not of a ghost, but of something much scarier."
    stop music
    play sound derrumbe
    show gabriel asustado at centroDer with dissolve
    Jock "No. Nonononono."
    play music tense_loop
    hide gabriel
    "At that moment, we all knew this with certainty."
    "Somewhere behind us, part of the tunnel had collapsed."
    "The choice now was simple."
    "The place we stood in currently made for a brief respite from the narrow tunnels."
    "Wide enough for four people to stand shoulder to shoulder, long enough that the two distinct parts of our group could glare daggers at each other from each end."
    "And at each of those ends stood an exit to this particular room."
    "Either we went back the way we came, or walked further into the unknown."
    "What would it be, Door A or Door B?"
    "A simple enough choice."
    show abril asustada at centroIzq with dissolve
    show gabriel asustado at centroDer with dissolve
    Darks "I am {i}not{/i} going back through there!"
    show abril enojada
    show gabriel enojado
    Darks "Didn't you fucking hear it collapse? It was literally a minute ago."
    show gabriel enojado2
    Jock "Of course I heard all that noise, who wouldn't!?"
    Jock "But that doesn't mean the tunnel has totally collapsed!"
    Jock "What I know for sure is that I am not staying here a minute longer."
    Jock "And I'm definitely not going deeper into this death trap!"
    show martina enojada3 at right with dissolve
    "Martina walked closer to Gabriel with a little box in her hand."
    "It was a matchbox."
    "In one quick motion, she struck a match to its side, a warm light emanating from it."
    "Gabriel stared at her, exasperated."
    show martina enojada2
    Pastel "Don't you see? The flame is moving towards that side."
    "She pointed at the exit that would take us deeper into the tunnels."
#[pan to tunnel 2 SI SE PUEDE!!! Si no llegamos no pasa nada] #INTEGRAR
    #scene bg tunel2
    #pause(5.0) ?
    #ADD stuff
    show martina enojada2 at right with dissolve
    show gabriel enojado at centroDer with dissolve
    show abril enojada at centroIzq with dissolve
    show santiago sorprendido at left with dissolve
    Pastel "That means that's where the airflow is going! There's bound to be an exit if we follow this tunnel."
    show gabriel sobrador
    Jock "You're an expert caver now?"
    show abril enojada
    Darks "She knows more about this than you, clearly."
    show gabriel enojado3
    Jock "You-"
    ##playaudio sfx tos?
    "Santiago cleared his throat, and four pairs of eyes turned to stare at him. He was clearly wilting under all the attention, but still continued."
    show gabriel forzada
    show martina enojada3
    show abril exasperada
    show santiago neutral
    Emo "We could check the entrance where we came from first... just to see if it collapsed or not."
    show santiago neutral2
    Emo "And if it did, we could double back and go the other way...?"
    #ADD scene bg tunel2
    hide gabriel
    hide santiago
    hide martina
    hide abril
    "A tense silence fell over us again."
    "My eyes went back and forth taking in Abril, Martina, and Gabriel's blank faces."
    "Wait, were we actually making progress?"
    "I thought we may have found a plan that no one could disagree on from the least likely source, but-"
    show martina enojada2 at right with dissolve
    show gabriel enojado at centroDer with dissolve
    show abril exasperada at centroIzq with dissolve
    show santiago at left with dissolve
    Darks "I'm {i}NOT{/i} doubling back to the structurally unsound cave-in hazard."
    Darks "I'm not willingly walking that way when we have actual proof that some part of it is collapsing."
    show gabriel enojado3
    Jock "And I'm not willingly following your stubborn ass into a death trap!"
    show gabriel enojado2
    Jock "Whatever, you want to go in there? Go, then."
    Jock "Santiago and I are going back the way we came."
    show santiago triste2
    Emo "..."
    show gabriel enojado
    Jock "You two,"
    "He pointed at Martina and me."
    show gabriel forzada
    Jock "Are welcome to come with, but I'm not going anywhere with {i}her.{/i}"
    show gabriel forzada2
    Jock "Hope you have a fun time playing in your creepy cave."
    "Abril did not look impressed."
    show abril desafiante
    Darks "Are you done?"
    "I expected another round of arguments to ensue from that response alone, but Santiago seemed to have foreseen that same future, reining in Gabriel's anger just barely by putting a hand on his shoulder."
    show gabriel forzada
    "Gabriel shook it off and clicked his tongue, but said nothing."
    "Abril narrowed her eyes at Santiago, who looked away."
    show abril exasperada
    Darks "You know you don't have to go with that asshole just because he says so, right?"
    show abril desafiante
    Darks "Whatever. I'm going that way. If you want to follow me, great. If not, that's on you."
    Darks "I'm done talking."
    hide abril
    "Throwing her hands up in the air, Abril walked over to the wall near her chosen tunnel and leaned against it, crossing her arms."
    "You could almost interpret it as her giving up, but both she and Gabriel kept glaring daggers at each other even then."
    show gabriel forzada2
    Jock "Alright, you three. Let's get going."
    "Perhaps Gabriel had interpreted the lack of response from the rest of us as tacit agreement to his plan, because he turned around to us with a grin that did very little to cover up from his still-very-obviously-simmering anger."
    "Santiago, who had been staring at the floor for a little bit now, nodded automatically, but Martina adjusted the straps on her backpack."
    show martina enojada2
    Pastel "Sorry, I'm going with Abi."
    show martina sonrisa
    Pastel "Take care of yourself, Santi. Alright?"
    hide martina
    "After a quick hug and an apologetic smile, she adjusted the backpack again and walked away towards the still-fuming Abril."
    show gabriel enojado
    Jock "Unbelievable."
    hide gabriel
    hide santiago
    show martina neutral at center with dissolve
    Pastel "So what do you wanna do, [Nombre]?"
    "All eyes turned towards me."
    "I was aware that I'd been entirely too quiet during this whole debacle."
    "The reality of it was that I was hoping they'd hash things out amongst themselves."
    "I didn't know these people."
    "I'd been doing what I'd been sent down here to do, yes, but I wasn't about to start taking sides until after I had all the facts."
    "And that moment was now."
    "Sighing, I resigned myself to make a decision."
    hide martina
    stop music
    menu branch: #implementar rutas
        "Go with Santiago and Gabriel":
            jump SantiGabi
        "Go with Martina and Abril":
            "Not implemented, sorry!"
            jump branch





    return

