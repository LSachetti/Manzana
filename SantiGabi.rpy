image white = "#ffffff"
image red = "#FF0000"
define dissolve2 = Dissolve(3.0)

#>Go with Santiago and Gabriel
label SantiGabi:
    "It was true that going back to the entrance seemed like the most reasonable choice to pick."
    "I didn't particularly care for Gabriel's tone but I supposed I would follow them around, just to see what happened."
    show santiago neutral at centroIzq 
    show gabriel enojado at centroDer
    "Adjusting the backpack on my shoulder, I turned to the brothers."
    MainC "Alright, lead the way."
    scene black
    pause (1.0)
    
    #[los mismos túneles de antes pero en reversa]
    scene bg tunel1 with wipeleft
    pause (1.0)
    scene bg entrada derrumbe with wipeleft
    "It wasn't long until we got back to the entrance."
    "That's what I would have liked to say, but..."
    show gabriel sorprendido with vpunch
    Jock "No. Nononono."
    show gabriel enojado2 with hpunch
    Jock "Goddamnit!"
    "Gabriel gawked at the now-covered-up entrance tunnel."
    hide gabriel with moveoutbottom
    #[sfx rocas?]
    "Santiago and I watched as he got on his knees and began to try and move the rocks out of the way with his bare hands."
    "But it was useless."
    "You couldn't fit a pin through some of the heavier-looking rocks."
    show gabriel 
    "Both of them looked lost in their thoughts."
    "I wondered what they wanted to do..."
    call screen charla_personajes("charlaSanti","charlaGabi",2,"Santiago sprites/santiago neutral.png",40,10, "Gabriel Sprites/gabriel neutral.png",1000,10)
    #[pausa hasta que cliqueás en Santiago o en Gabriel? Forma de hacer que la gente sepa que les pueden hablar?]
    #DIALOGO

label charlaGabi:
    Jock "..."
    #[sfx rocas moviéndose, se sacude la pantalla]
    show gabriel enojado at centroIzq with dissolve
    pause (0.5)
    show gabriel enojado2 at center with move
    pause (0.5)
    show gabriel enojado3 at centroDer with move
    show gabriel enojado3 with vpunch
    Jock "Can't you see I'm busy?!"
    hide gabriel
    "I decided to see what was up with Santiago…"
    call screen charla_personajes("charlaSanti","charlaGabi",1,"Santiago sprites/santiago neutral.png",40,10, "Gabriel Sprites/gabriel neutral.png",1000,10)

label charlaSanti:    
    #[si cliqueás en Santiago (sigue la historia)]
    "Santiago cleared his throat."
    show santiago with dissolve
    Emo "Gabi..."
    show santiago at centroIzq with move
    show gabriel enojado2 at centroDer with dissolve
    Jock "..."
    show gabriel enojado3
    Jock "What?!"
    Jock "I know it's useless! I know!"
    Jock "What am I supposed to do, lie down and wait to die?!"
    hide santiago
    hide gabriel
    "We could probably still catch up to Abril and Martina if we tried..."
    "But Gabriel would probably throw a fit at the idea."
    "Just as I was considering saying something about it, Santiago spoke up again."
    show santiago sorprendido with dissolve
    Emo "Was that always there?"
    "Gabriel didn't even look up, immersed as he was in his moving rocks from point A to point B."
    "Squinting, I followed the light coming from his flashlight."
    MainC "It definitely wasn't."
    show santiago sorprendido at centroIzq with move
    show gabriel enojado3 at centroDer with dissolve
    Jock "What in the world are you both yapping about?!"
    "Gabriel finally looked up. Then he froze."
    hide santiago
    hide gabriel
    scene black
    with flash
    scene bg tunel escondido with dissolve
    "With both my flashlight and Santiago's combined, we could finally see it properly."
    "An entrance to a tunnel that hadn't been there before had materialized on the rock."
    show santiago neutral with dissolve
    Emo "It might've been there but sealed before... maybe the cave-in uncovered it."
    "It was as good a theory as any."
    MainC "So, are we going through there?"
    show santiago neutral2
    Emo "...It's either that or we go back, I guess. We may be able to catch up."
    "Santiago arrived at the same conclusion that I had."
    show santiago neutral2 at centroIzq with move
    show gabriel enojado at centroDer with dissolve
    Jock "I am not going to go back there and play nice with them. No way."
    "He gave the new entrance a dubious glance before nodding to himself. Probably psyching himself up."
    show gabriel sonrisa2
    Jock "Alright. Random new tunnel it is. Let's go, Santi."
    hide gabriel with dissolve
    show santiago neutral
    Emo "..."
    "Santiago shot me an apologetic look, but followed suit."
    hide santiago with dissolve
    "..."
    "Well, I did need to stay close to them, in any case."
    "My steps echoed as we walked into the unknown."
    scene black with dissolve
    

    #[Empieza el laberinto]

    #[En un momento del laberinto, como en la mitad]
    #[event #1]
    scene black with dissolve
    "As we turned the corner, we were faced with impenetrable darkness."
    "We had been walking around these tunnels for a while, with our flashlights as the only weapon to cut through the inscrutable way ahead of us, our eyes adjusting to make out the shape of things."
    "So when we were faced with nothing but a pitch-black void, all three of us stopped in our tracks."
    show santiago sorprendido with dissolve
    Emo "Hello?"
    hide santiago with dissolve
    "Santiago called out, for some reason."
    "Gabriel scoffed, but I understood Santiago's thought process."
    "The feeble beam of light coming from our flashlights stopped a few meters in front of us, but not in the way that light naturally dimmed as it traveled away from its source."
    "No, it stopped abruptly."
    "Like something was there, blocking any and all illumination from going through."
    "..."
    "But there was no reply."
    "No movement."
    "No rocks shifting, no sudden breath caught in some being's throat."
    show santiago neutral with dissolve
    Emo "..."
    MainC "..."
    "After a few seconds of waiting for a response, Gabriel broke the silence."
    show santiago neutral at centroIzq with move
    show gabriel sonrisa2 at centroDer with dissolve
    Jock "So, are you both done being scaredy cats?"
    MainC "Don't you think that's weird?"
    "I gestured towards the impenetrable darkness with my flashlight."
    show gabriel enojado
    Jock "I think this whole night has been weird."
    Jock "That's why I'm getting the fuck out of here."
    Jock "If you chickenshits want to stay here and wallow, fine."
    show gabriel sonrisa2
    Jock "I'm outta here."
    "He took one step forward."
    show gabriel sorprendido with vpunch
    show gabriel asustado
    hide gabriel with moveoutbottom
    #[sprite shows for one second and then disappears (maybe with a shaking animation or smth like that?), there's a yelp]
    show santiago asustado
    Emo "Gabi?!"
    "Gabriel's silhouette had been there one minute, gone the next."
    Emo "Are you okay?! I can't see you!"
    hide santiago
    "The not-so-comforting blanket of silence fell over us as we waited for a response."
    "And then-"
    with vpunch
    Jock "FUCK!"
    with vpunch
    with hpunch
    Jock "FUCK! SHIT GODDAMN IT MOTHERF-"
    "The cursing was punctuated every time with groans of pain."
    show santiago sorprendido with hpunch
    Emo "Where are you?!"
    hide santiago
    "I pointed my flashlight to the ceiling, then to the floor."
    "That's when we saw him."
    show gabriel enojado2 with dissolve
    "Gabriel was at the bottom of a pretty big drop, a few meters down, very much alive."
    "His foot, however..."
    show gabriel enojado3
    Jock "Stop shining that shit in my face!"
    Jock "Fucking hell."
    hide gabriel
    "There was no pretty way to describe it."
    "It was on backwards."
    "A completely messed-up and broken ankle, the kind of fracture that would probably require surgery to heal."
    show santiago sorprendido with hpunch
    Emo "I'm coming! Stay still!"
    "Santiago pointed his flashlight at the ground below us."
    "It was a big drop if you were walking without paying attention, but not so steep that we couldn't find a way down if we were more careful."
    show santiago neutral2
    "We nodded to each other."
    hide santiago with dissolve
    "Carefully feeling the rock wall for purchase, we made our way down to Gabriel. First Santiago, then myself."
    "By the time I reached both of them, Santiago was already busy at work applying a makeshift splint on Gabriel's leg, who was bearing the pain through gritted teeth."
    MainC "That's impressive. I wouldn't know where to start with a break so severe."
    show santiago neutral2 with dissolve
    Emo "Oh, I'm a nursing student."
    show santiago neutral
    Emo "And I figured something would happen, so I brought some stuff..."
    show santiago neutral at centroIzq with move
    show gabriel triste at centroDer with dissolve
    Jock "He's always-"
    show gabriel enojado3
    Jock "-Augh."
    show gabriel triste
    Jock "He's always carrying that stuff around."
    Jock "I told him he wouldn't need it, that it would only slow him down."
    show gabriel feliz
    Jock "Glad you didn't listen, for once."
    show santiago 
    Emo "I told you, it's better to be prepared."
    MainC "..."
    menu:
        "Now Gabriel is the one who is going to slow us down.": #(+1 drop Gabriel)
            jump dropGabriel1
        "Guess we should've listened to Santiago all along.": #(+1 push Santiago)
            jump pushSanti1
    

label contEvent1:
    scene black with dissolve
    "With Gabriel now limping in his improvised splint, we couldn't scale the rock wall back up."
    "And there had been no way to go through back then, anyway."
    "The darkness that had enveloped us had dissipated with Gabriel's fall, like fog suddenly lifting."
    "So we decided to explore the new area we were in a little more."
    "Luckily, we hit the jackpot."
    show santiago sonrisa with dissolve 
    Emo "Over there. Is that a way out?"
    scene bg tunel1 with dissolve
    "We pointed our flashlights towards a particular section of the rock."
    "The opening was a tight squeeze, but it was definitely big enough to fit us."
    "And we were out of options."
    MainC "I guess so."
    MainC "We should try it out."
    "Once again, we set out to walk deeper into the belly of the beast."
    scene black with dissolve
    jump event2
    #[fin event #1]

    #[event #2]
label event2:    
    scene bg tunel2 with wipeleft
    pause (0.5)
    scene black with wiperight
    #[sfx pasos]
    "It had been several hours of nothing but walking by now."
    "Our feet ached from stumbling around, unseeing, our hands used to the sharp sting of rocks cutting into them from holding onto the walls as we felt for something, anything."
    "Anything to guide us in the dark."
    "It was as if we had forgotten what sunlight was."
    scene white with dissolve
    scene bg luz salida with dissolve
    "Which is why when we turned a corner and saw light at the end of the tunnel, we were terrified."
    show santiago asustado at centroIzq with dissolve
    show gabriel sorprendido at centroDer with dissolve
    "Two of us were, at least."
    show gabriel sonrisa2
    Jock "The exit...!"
    with vpunch
    "Eyes ecstatic, Gabriel lurched forward, almost making Santiago tumble down to the floor."
    hide gabriel with dissolve
    "Luckily Santiago regained his balance in time, but that was enough opportunity for Gabriel to break free and start limping towards the light source."
    show santiago asustado with hpunch
    Emo "Wait!"
    "By the time he shouted that, Gabriel was already almost at the light."
    show gabriel feliz at centroDer with dissolve
    Jock "I can see it! There's an exit!"
    Jock "Hurry the hell up!"
    show gabriel sonrisa2
    Jock "I'm not waiting for your slow asses!"
    hide gabriel
    hide santiago
    "We had no choice but to follow him."
    show santiago with dissolve
    "Santiago got there first and stopped in his tracks, turning back nervously to me."
    "Like he wanted to confirm something."
    "I caught up to the both of them as fast as I could."
    scene white with dissolve
    pause (1.0)
    "Pure white burned my eyes for a second."


    #[fondo blanco de repente con una transición o algo]


    "It was so bright that I had to blink one, two, three times..."
    "Until my eyes adjusted to the scene."


    #[transición a fondo medianamente lenta]
    scene bg final gs1 with dissolve2

    MainC "..."
    "I couldn't believe it."
    "The exit was... right there."
    "Scarcely 10 meters away from us, the tunnel widened, bringing in the first rays of sunshine."
    "It was dawn already, but even from here I could hear the distant noise of the city, of crickets, of life."
    "And the only thing that separated us from that..."
    "... Was a steep rock wall. Steep, so steep..."
    show gabriel asustado at centroDer
    show santiago at centroIzq
    "I could see it in Gabriel and Santiago's faces."
    "The hope of finding their heart's greatest desire, the utter despair of knowing the ordeal wasn't over yet."
    "We'd have to climb. There was no other way around that."
    "And if we slipped even once..."
    scene black with dissolve
    "I pointed my flashback at the hungry mouth, rock-sharp teeth all over it, ready to devour us."
    "The light didn't touch the bottom."
    scene bg final gs1 with dissolve
    show santiago at centroIzq
    Emo "..."
    show santiago neutral2
    Emo "... I'll go first."
    "His words startled me out of my thoughts."
    show gabriel sorprendido at centroDer with dissolve
    "Gabriel opened his mouth to reply, but Santiago cut him off."
    show santiago
    Emo "You can't climb with your foot like that."
    show santiago neutral2
    Emo "I have a rope in my backpack. I'll climb to the top and lower it for you two."
    show gabriel triste
    Jock "That..."
    "He opened his mouth again, then closed it."
    "Whatever demons Gabriel was fighting, it seemed like he kept a level head through it, because he gave his brother a stiff nod."
    show gabriel neutral
    Jock "Be careful."
    show santiago neutral
    Emo "... Alright."
    scene bg final gs1 with zoomin:
        zoom 2.0
    #C: queria hacer un efecto como de que sube pero no se como je
    "Watching him climb was nerve-wracking."
    "Santiago had started off strong, finding purchase for his hands and feet with relative ease."
    "The rocks at the starting level, which jutted out a little more, were a bit more firm."
    "But that wasn't the case for the rocks further up."
    show santiago sorprendido with dissolve
    Emo "...!"
    hide santiago asustado with hpunch
    show gabriel asustado at centroDer with vpunch
    Jock "Santi!"
    "Gabriel jolted upright when Santiago's hand slipped."
    "The wall was slicker up there, the kind of rock wall that even people with climbing experience and equipment would need to tackle carefully."
    hide gabriel
    show santiago asustado at centroIzq with vpunch
    "Santiago's balance was thrown off by the sudden lack of support."
    with hpunch
    with vpunch
    "He flailed around, hand grasping the air desperately."
    "Holding on to a little bit of hope before inevitably slipping off again."
    "Once, twice..."
    "Our eyes couldn't help but fixate on his far-up figure, already imagining the fall."
    "And then-"
    show santiago triste2
    Emo "...!"
    "-a miracle."
    show santiago neutral2 at centroDer with move
    "Lurching forward one more time, Santiago grabbed onto something."
    "The sigh Gabriel released told me he had been holding his breath all that time."
    show santiago
    "After stopping for a second (probably to regain his breath), Santiago climbed up the last meter or so, making it to the top."
    scene bg final gs1 with dissolve
    "He was sweaty and clearly out of breath, but he was alive."
    "Santiago ducked out of view for a few seconds, and then returned, beaming, and let down one end of the rope."
    show gabriel feliz with dissolve
    "Gabriel laughed."
    Jock "We're saved!"
    Jock "He did it, that little fucker!"
    "The moment Gabriel grabbed onto the rope, I stopped him."
    MainC "Let me go up first."
    show gabriel neutral
    pause (0.5)
    show gabriel enojado2
    "It was as if I had punched him in the gut."
    "I watched his expression turn into something angry, ugly."
    Jock "What the hell, why you?"
    show gabriel enojado3
    Jock "I want to get the fuck out of here, too!"
    "I'd have to be clear about this."
    "If he fought me on this and I let him get his way, neither of us would make it out of here."
    MainC "You have an injured foot."
    MainC "Severely injured, at that. You won't be able to climb."
    MainC "Santiago will have to pull you up. You know that, right?"
    "Some of it may have gotten through to him, because he let go of the rope, albeit reluctantly."
    show gabriel enojado
    Jock "So why does that mean it has to be you next, huh?"
    Jock "He can pull me up, then you can climb."
    MainC "Wouldn't it be easier if there were two people up there to pull you up?"
    MainC "Not to mention safer."
    show gabriel enojado2
    "Red with anger, yet unable to refute my points, Gabriel balled his fists."
    "Resting against the rock wall as he was, his weight entirely on his uninjured foot, he must've been well aware that he couldn't make it up there without help."
    show gabriel enojado
    "Ultimately, he clicked his tongue and nodded my way."
    Jock "Whatever. Hurry the hell up."
    pause (1.0)
    scene bg final gs1 with dissolve
    scene bg final gs1 with zoomin:
        zoom 1.5
    MainC "..."
    "Having watched Santiago climb up, and having tied the rope around myself, I was a lot more prepared than he had been when he tackled this wall."
    "So despite how much my muscles burned every time I pushed myself up to another small ledge, I made quick work of getting all the way up."
    scene black with dissolve
    show santiago feliz with dissolve
    "When I arrived, Santiago smiled at me and helped me get untied."
    "Now there was only one more thing to be done."
    scene bg final gs2 with wipeleft
    pause (0.5)
    scene bg final gs1 with wipeleft
    show gabriel neutral with dissolve
    "We saw the far-down Gabriel grab the end of the rope, tying it to his waist as best he could."
    scene bg final gs2 with dissolve
    "When everything was ready, Santiago and I began pulling."
    "Pulling up a grown man, even between two people, is no easy feat."
    "Santiago didn't have a second pair of gloves, so he gave me some rags to put between my hands and the rope."
    "Even then, it still dug into my skin, making cuts I couldn't see but could definitely feel."
    "We had been going at a slow and steady pace, when we heard the growl."
    #sfx growl
    with vpunch
    with hpunch
    with vpunch
    show santiago sorprendido with dissolve
    Emo "...!"
    show santiago triste2 with vpunch
    "Startled, Santiago dropped a few centimeters of rope before he caught it again."
    scene bg final gs1 with vpunch:
        zoom 1.5
    show gabriel asustado
    pause (0.5)
    "I saw Gabriel jerk in absolute pain on the other end, the movement slamming him (and his injured foot) against the wall."
    show gabriel enojado3 with vpunch
    Jock "Get me out of here!!"
    Jock "Santiago pull me the fuck up!"
    scene bg final gs2 with hpunch
    "We quickly got back into action, pulling the rope as quickly as our arms would allow."
    with vpunch
    with hpunch
    with vpunch
    "In the distance, we heard steps like drums, like thunder."
    "Steps so heavy, they couldn't be from anything even resembling a person."
    scene bg final gs1 with vpunch:
        zoom 1.5
    show gabriel asustado
    Jock "There is something down here with me, get me the hell up!"
    with vpunch
    with hpunch
    with vpunch
    "The sound drew closer, closer still."
    scene bg final gs2 with dissolve
    "Gabriel was almost at arm's reach."
    show santiago triste2 with vpunch
    "Santiago extended his hand, grasping Gabriel's..."
    Emo "...!"
    show santiago asustado with hpunch
    "His hand slipped."
    "It was covered in sweat from the exertion, the fear."
    with vpunch
    with hpunch
    with vpunch
    "The cave vibrated around us. We needed to get out as soon as possible."
    "Santiago's hand was still hanging in the air."
    "He leaned down to pull Gabriel up..."
    $ decisionFinal(pushSanti, dropGabriel)