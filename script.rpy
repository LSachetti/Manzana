#py # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default prn = "Test"
default Nombre = "Beto"
define canal = "PlaceHolder"
define petNemo = "Santi"
define MainC = Character("[Nombre]")
define Emo = Character("Santiago")
define Jock = Character("Gabriel")
define Darks = Character("Abril")
define Pastel = Character("Martina")
define OtroCam = Character("[prn]")



# The game starts here.

label start:
    menu:
        "Tester"

        "Texto":
            jump Texto
        "Laberinto":
            jump Laberinto
        "Test Rollback":
            jump Rollback


label Texto:
    scene bg room
    show eileen happy

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
    MainC "\"The tunnels, how deep do they go?\""
    "..."
    #MC
    "A hand grabbed at my shoulder."
    MainC "\"Augh?!\""
    "Taken aback, I spun around on my heels."
    "Four people in total stood there, gaping at my reaction."
    "I must've really been zoning out, if a group this big could sneak up on me."
    #[Pastel sad sprite]
    Pastel "\"Aww, you scared him, Jock.\""
    #[sprite del chabón a la defensiva]
    Jock "I didn't mean to."
    #[sonrisa]
    Jock "Excuse me, are you nombredelcamarógrafo?"
    MainC "Huh?"
    Darks "We know [prn], that's not [prn]."
    Emo "But [prn] has/have a camera..."
    "I focused on what they were carrying."
    "All four of them had hefty backpacks and a camera of their own. That's when it hit me."
    MainC "Ah, it's you lot. I've been waiting for you."
    MainC "[prn] sent me, actually. He said he couldn't make it."
    "[Darks] sighed."
    Darks "Yeah, that tracks."
    Darks "I told you all he'd flake."
    Emo "Did he say what happened...?"
    "I thought about it."
    MainC "Not really, but he sounded like he wasn't super psyched about it."
    MainC "We're filming inside the tunnels, right?"
    Pastel "Yeah!"
    Pastel "This place is going to be crawling with people next week."
    Pastel "So we figure if we want to explore them, it's now or never!"
    Pastel "I'm [Pastel], by the way! And these are..."
    Pastel "[Darks]," #[mostrar sprite de la Darks]
    Pastel "[Emo]," #[mostrar sprite del Emo]
    Pastel "And [Emo]'s brother." #[mostrar sprite Jock]
    #[Jock irritado pero con una sonrisa]
    Jock "It's [Jock], actually."
    MainC "[MainC]. Nice to meet you all."
    MainC "Anyhow, if we're going to go in, you came here at the right time."
    Darks "Why is that?"
    MainC "Because it's almost dinnertime."



    #ESCENA 2
    #jump? label scene2?
    "Sneaking in was even easier than I thought it would be, especially with a group this large."
    "We ran in one by one, waiting to see a flashlight signaling us before sending each and every member of our group."
    "I was the last one in, my eyes struggling to get used to the darkness. And it didn't help when someone flashed their flashlight right into my eyes."
    Pastel "Woops, sorry!"
    MainC "D-Don't worry about it..."
    "I tried to be reassuring, knowing that she couldn't see me blinking the tears forming at the corners of my eyes away."
    "That's when I remembered what I was supposed to be doing. I turned my camcorder back on, and though I specifically brought one that was good in low light settings, it was still extremely dark in here, so I turned on my flashlight as well."
    "The walls, made out of something closer to clay than stone, were narrow around us, closing in on us like an unnerving hug."
    "Behind us was the light of the entrance. In front of us, an impenetrable darkness that even our flashlights couldn't cut through."
    "We all stared ahead for a second, until someone broke the silence that had fallen over us."
    Darks "Alright, let's go."
    Darks "If we stay this close to the entrance, sooner or later someone will notice we're in here. We need to go deeper."
    "Making sure everything was in working order, we braved the darkness up ahead."
        #[sfx de pasos con eco, pasan un par de fondos de pasillos distintos]
    "It hadn't been five minutes when a creepy voice from behind me broke the silence."
    Emo "Have you heard of the legend, then?"
    MainC "?!"
    "I startled so bad I accidentally bumped into [Pastel], who yelped."
    Jock "Haha, good one, [Emo]."
    Jock "You scared [MainC] half to death."
    Emo "I was just trying to make conversation..."
    Emo "Sorry about that."
    MainC "It's okay."
        #[más sfx de pasos]
    MainC "I wasn't aware that there was some sort of legend about this place, though. With it being so recent and everything."
    Emo "Well, it's more like an urban legend that popped up these last few weeks, I guess."
    "[Pastel] giggled."
    Pastel "A place this creepy has to have something going on!"
    Darks "You're only saying that because it's old."
    Darks "People will make all sorts of shit up if a place is old enough."
    Emo "Maybe, I don't know."
    Emo "But there've been disappearances around the house that used to be on the entrance even before they found the entrance..."
    Emo "And-ugh."
    "[Darks] stopped walking all of a sudden, causing a chain reaction of collisions."
    Pastel "A little heads up next time would be nice!"
    Darks "Oh, please."
    "The area ahead of us was wider than the narrow tunnels we'd been trudging through, almost like a resting stop. Definitely big enough that we wouldn't have to be staring at each other's backs."
    "[Darks] turned around."
    Dark "We can do it here."
    "Everyone but me murmured in agreement."
    MainC "What are we doing, exactly?"
    "The only thing I knew was that they wanted me to record this place."
    Jock "Did [prn] not tell you anything?"
    "[Pastel] hit him on the arm."
    Pastel "We're making a YouTube video!"
    Pastel "We're into like, you know... cryptids, urban legends, all that sort of supernatural stuff."
    Darks "You are into that sort of supernatural stuff."
    Jock "All I signed up for was to drive all of you here."
        #[Sprite del emo pero más chiquito que los demás y la voz más bajita]
    Emo "I think the supernatural is pretty cool..."
    Pastel "You guys are all boring."
    Pastel "Whatever, I'm over it."
    Pastel "Everyone take positions! We're going to start now!"
    "[Jock] surreptitiously stood behind me as I lifted my camera, still rolling, towards the other three."
    Pastel "Aaand... action!"
    Pastel "Welcome to [canal], your weekly fix of the scariest places right here in your vicinity!"
    Emo "Today we are exploring the cavernous expanse of a certain tunnel... I'm sure you know which one if you've been looking at the news."
    "[Jock] scoffed, and not quietly."
    "They're going to have to fix that in the edit."
    "I can't blame him for that reaction though. It is creepier that he can switch it up on command..."
    Darks "And if you don't know, you should be paying more attention to the world."
    Darks "Go watch the news for a change."
    Pastel "After you watch the show of course."
    Emo "Don't forget to leave a like and subscribe!"
    "The three of them stood there smiling (well, two of them were smiling at any rate) for a second too long, like they were waiting for something..."
        #[SFX clapping hands]
    Pastel "Alright, I think that's good for now."
    Darks "Not our worst intro."
    Emo "Maybe we could get some b-roll next?"
    "I spent the next few minutes on auto-pilot, pointing my camera at whatever needed to be shot. For such an interesting location, it was quite a mundane affair."
    "Until Martina, who I was quickly realizing ran the ship for the most part, clapped her hands again."
    Pastel "Alright, we should get on with it then. Did you bring the thing, [petNemo]?"
    "I instinctively pointed my camera at him. He nodded."
    Emo "I stayed up late making it last night..."
    "Saying this, he produced a strange cloth doll, tied tightly all around its chest with thread."
    "I immediately knew what it was."
    MainC "Are you guys going to try the ritual?"
    Darks "Not much else to do down here."
    Darks "Unless we want to post a video of us walking around in the dark for two hours."
    "I should've known. Every time I go online these days someone is passing that one ritual around, and from what I've heard from them we must move in similar circles."
    "However, I was curious..."
    MainC "You do know about the disappearances, right?"
    Jock "Oh, here we go again."
    "[Jock] ran a hand through his neat hair with the exasperation that only someone who heard a story a million times and liked it less in every opportunity could have."
    "And judging by [Emo]\'s guilty look, I was pretty sure that was the case."
    Darks "Come on."
    Darks "All those zero-karma accounts who dropped off the internet were clearly trying to drum up hype."
    Emo "To be fair, from what I researched the disappearances were happening before the first thread was posted..."
    "[Darks], who had been crouching and lighting a candle on the ground rose back to her feet and promptly rolled her eyes."
    Darks "There are no supernatural disappearances."
    Darks "People are just retroactively linking the tunnel with random missing people through the years because it makes for a better story."
    Darks "All the more reason to perform this so-called ritual."
    Darks "So that people can see it's not real."
    "Those words reverberated in the empty hollowness of the tunnels."
    "In our silence, all we could hear was the echo of those words, getting farther and farther away."
    "And on everyone else's faces, a question began to form."
    "But what if it is real...?"
    "Gabriel cleared his throat."
    Jock "Can we like, get on it then?"
    Jock "I don't wanna be here all night."
    "He was right."
    "I lifted my camera as Martina grabbed the doll in steady hands, a look of determination on her face."
    "The ritual was about to begin."


        #Escena 3???
    "The whole thing was quite simple."
    "The doll was bound fourteen times with thread."
    "Someone would walk around the candle fourteen times."
    "And every time..."
    Pastel "The door stands open."
    "[Pastel] would unravel one loop of thread from the doll, chanting."
    Pastel "There is no lock."
    "More thread was stripped off the doll."
    "Another circle."
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
    "[Pastel] stopped in her tracks."
    "The thread came off the doll completely."
    "I followed her with my camera as she crouched near the flame, the two ends of the thread in each of her hands. She closed in near the fire..."
    "...and it burned it through, snapping it in two."
    Pastel "Thus we step now over the threshold, O son of kings and queens. May you welcome us in."
    "And she, too, fell into the all-encompassing silence we had been submerged into."
    "It could all have ended there."
    "The quiet overpowering us for one final moment as the video ended."
    "You couldn't ask for much more material for ghost hunting-type viral videos unless you were thinking of faking evidence."
    "But-"
    "At that precise moment, the rumbling began."
    "Not of a monster, not of a ghost, but of something much scarier."
    #[sfx PIEDRASSS COSAS NO SÉEE Pau confío en tu criterio y expertisse]
    Jock "No. Nonononono."
    "At that moment, we all knew this with certainty."
    "Somewhere behind us, part of the tunnel had collapsed."


    return

label Laberinto:

    "Implementar"

    return


label Rollback:

    $ persistent.message = 'non rollback'
    'foo'
    'bar'
    $ if renpy.in_rollback(): persistent.message = 'rollback changed message'
    '[persistent.message]'
    'foo2'
    'bar2'

    return
