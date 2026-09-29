label santigoOpt1:
    MainC "So, who's older?"
    "Santiago turned to look at me, clearly startled."
    "Whether he was confused by my question or just startled that I would talk to him at all, I wasn't sure."
    Emo "Uh, we're twins...?"
    MainC "I mean yeah, I can tell."
    "Even through all the make-up and different attitudes, that much was obvious to me."
    MainC "But there's always an older twin and a younger twin."
    Emo "A few minutes don't make that much of a difference."
    MainC "Ah. You're the younger one."
    "Santiago huffed. It looked like I'd hit the nail on the head."
    MainC "That does explain a lot."
    Emo "What do you mean?"
    "Seemed like this was a sore spot."

    menu:
        "He's always looking out for you.":
            if dropGabriel > 0:
                $ dropGabriel -=1
            MainC "... I mean, you seem a little jumpy."
            MainC "He may be trying to take charge so you can be more at ease."
            Emo "..."
            "Santiago flashed me a guilt-ridden smile."
            Emo "Yes, he's always doing that."
            Emo "He's been like that since we were little."
            MainC "Must be nice to be so close."
        "He's always telling you what to do.":# (+1 drop Gabriel)
            MainC "... I mean, he won't stop barking orders at you."
            "Santiago didn't reply at first. His face took on a pensive look."
            Emo "It's not like that. He's just trying to help."
            MainC "If you say so."
            Emo "..."
            Emo "Gabi can be a bit grating, but he's a good guy..."
            MainC "Alright. I'll give him another chance, then."
 
            $ dropGabriel +=1
    
  
label gabrielOpt1:
    #[Talk to Gabriel #1]
    MainC "So, you're twins, huh?"
    Jock "Yeah."
    Jock "I'm the older one."
    "I could surmise that much."
    MainC "It must be fun to be that close, age-wise."
    Jock "Hah. Fun."
    Jock "Only child, I take it?"
    MainC "Yup."
    Jock "There's your problem. Sure, there are times when it's fun, but others? Man."
    "He shook his head."
    Jock "What do you think siblings do that's so much more fun than being by yourself?"
    MainC "..."
    menu:
        "They play together.":# (-1 push Santiago)
            if pushSanti > 0:
                $ pushSanti -=1
            MainC "I often played all by myself as a kid."
            MainC "My mom couldn't catch a break. I was always telling her I wanted a sibling to play with."
            MainC "Ultimately I did get a pet but it just wasn't the same, you know?"
            MainC "If I threw a ball at him he'd bite right into it."
            "To my surprise, Gabriel laughed."
            Jock "We are the same in that regard, then."
            Jock "Santi wasn't much for sports. I had to wait to be in school to start rugby."
            Jock "But we did play other games."
            "He grinned and closed his eyes, lost in reminiscence."
            Jock "We used to drive everyone mad by pretending to be one another."
            Jock "That's what finally got my mom to stop putting us in matching outfits."
            Jock "Then he started dyeing his hair, though. Couldn't really pull it off after that."
            "What a heart-warming anecdote."
        "They have each other's backs.":# (+1 push Santiago)
            $ pushSanti +=1
            MainC "I mean, it's not necessarily fun but I figure it must be nice to be able to depend on someone else."
            MainC "Being so close you can trust each other to have your back and all that."
            MainC "And of course, knowing someone trusts you enough to rely on you."
            Jock "Ha!"
            Jock "It does sound nice, having someone you can count on."
            MainC "... Santiago seems to rely on you enough."
            "Gabriel sighed, all traces of his previous humor gone."
            Jock "He does, doesn't he?"
            Jock "Sometimes I wonder what he'd do without me..."
            "Gabriel fell into a contemplative silence that I didn't dare to break."

    
label santiagoOpt2:
    MainC "So, why Gooptube?"
    "Santiago looked back at me."
    "The look in his eye told me that he had been expecting me to ask this at some point."
    Emo "You mean, I don't seem like the type?"
    MainC "I hope that's not too weird to ask."
    Emo "Nah, it's fine."
    Emo "..."
    Emo "The girls sort of suggested it once when we were hanging out."
    Emo "They said it could be fun."
    Emo "I wasn't sure at first but I ended up agreeing."
    Emo "I guess it was to get out of my comfort zone... kind of."
    Emo "And then it stuck."
    menu:
        "It doesn't seem like it helped":# (+1 drop Gabriel)
            $ dropGabriel +=1
            MainC "Did it help?"
            Emo "...Huh?"
            MainC "I mean, you look different on camera."
            MainC "And I don't know you."
            MainC "But you don't look that confident when the camera isn't rolling."
            Emo "..."
            MainC "Sorry."
            Emo "No, it*s true."
            Emo "I guess I haven't fully come out of my shell yet."
        "You change on camera":# (-1 drop Gabriel)
            if dropGabriel > 0:
                $ dropGabriel -=1
            MainC "You completely transform while on camera."
            MainC "I was kind of impressed."
            "I hadn't known him for that long, but even I could tell that the smile Santiago gave me was not a common sight."
            Emo "Heh. Thanks."
            Emo "It might not seem that much to some people, but I feel like I've changed a lot from when I started doing it."
            Emo "Having the girls and Gabi there for me while I do it has been the only reason I've made it this far."
            MainC "Nice to have people who care about you, huh?"
            


label gabrielOpt2:
    MainC "You know, I still haven't figured it out."
    Jock "Figured out what?"
    MainC "Y'know."
    MainC "I get why they're here if they're into spooky stuff and the like."
    MainC "But you didn't seem to be enjoying yourself."
    Jock "Ha."
    Jock "And you're right about that."
    "Gabriel rolled his eyes and sighed."
    Jock "I didn't want to come, but Santi asked me to."
    Jock "Had to drive all of them here."
    Jock "And are they grateful for it? No."
    menu:
        "The girls were a bit harsh on you": #(-1 push Santiago)
            if pushSanti > 0:
                    $ pushSanti -=1
            MainC "I guess the girls weren't all that grateful, no."
            MainC "They don't seem to like you much, actually."
            Jock "You got that right."
            Jock "You couldn't catch me dead hanging out with the freakshow."
            Jock "But Santi really came through, huh?"
            MainC "What do you mean?"
            Jock "When push came to shove and his friends were on my ass, he backed me up."
            "With a swift movement he threw his head back and cackled."
            Jock "The look on Abril's face when she realized Santi was coming with me was {i}priceless{/i}"
            Jock "Didn't think he had it in him!"
            "It was a weird thing to be celebrating."
            "But if he was happy, I supposed it was fine..."
        "You really stepped up":# (+1 push Santiago)
            $ pushSanti +=1
            MainC "Yeah, they don't seem to like you, and vice-versa."
            Jock "You got that right."
            Jock "You couldn't catch me dead hanging out with the freakshow."
            MainC "Yet you toughed it out for your brother, huh?"
            MainC "I'm impressed."
            "Glancing at Santiago surreptitiously, Gabriel clicked his tongue."
            Jock "Not like it's the first time that's happened."
            Jock "And look where that got me."
            Jock "Now I'm down here, inhaling dust."
            Jock "Honestly, why did I put myself through this...?"
            "Gabriel didn't look like he wanted to talk much after that"
            
label santiagoOpt3:

    MainC "Do you two get along usually?"
    Emo "That's... a really forward question."
    MainC "We've been doing nothing but walk for a while now."
    MainC "I'm bored."
    Emo "Hmm."
    Emo "Maybe I should be the one to ask you something, then."
    "There was a note in Santiago's voice that I couldn't place."
    "His voice was hesitant, as usual, but there was something else in there."
    "Like he was finally finding an opportunity to express something he'd been thinking about."
    "It was a bit unnerving, and it felt like I was walking into an ambush."
    "Still, I figured there wasn't much harm in it."
    MainC "Alright, shoot."
    "A small pause."
    Emo "Did you really come here to cover for Facundo?"
    menu:

        "Yes": #(-1 drop Gabriel)
            if dropGabriel > 0:
                        $ dropGabriel -=1
            MainC "What kind of question is that?"
            MainC "He let me know earlier today that you'd need a camera."
            MainC "I didn't have anything better to do."
            Emo "..."
            Emo "I see."
            Emo "It's okay, you don't have to tell me if you don't want to."
            MainC "..."
            Emo "Regardless of your intentions when you brought us down here, we're all in this mess together, aren't we?"
            "There was a cold glint to Santiago's face as he smiled."
            Emo "So it's fine. I won't press you about it anymore."
            Emo "I think I'm done talking."
        "No":# (+1 drop Gabriel)
            $ dropGabriel +=1
            MainC "..."
            Emo "..."
            MainC "..."
            MainC "No, he didn't."
            "Santiago sighed. To my surprise, it didn't seem to be out of dismay or frustration."
            "It was a sigh of relief."
            Emo "I knew as much."
            MainC "What gave me away?"
            Emo "Oh, nothing really. You were really believable."
            Emo "I suspected something was weird, but I only put it together down here."
            MainC "..."
            Emo "Is your name even [Nombre]?"
            MainC "..."
            MainC "No, it's not."
            Emo "I see."
            Emo "Don't worry."
            Emo "I won't tell Gabi."
            MainC "...Why?"
            "In the darkness, with only the flashlights as our light source, I couldn't tell what lurked behind Santiago's eyes."
            Emo "Because you told me the truth."
            Emo "And I understand being a different person to different people."
            MainC "...Thanks."


label gabrielOpt3:
    MainC "...!"
    "I had approached Gabriel to talk, but the moment I entered his field of view, his mouth opened automatically."
    Jock "So hey, what do you think of Santi?"
    MainC "..."
    MainC "That's a really forward question, isn't it?"
    Jock "What, so only you get to pick my brain?"
    Jock "You've been asking me non-stop questions ever since we got stuck here."
    MainC "Fair enough."
    "Gabriel drummed his fingers against the rock wall impatiently."
    Jock "So?"
    MainC "I was thinking."
    MainC "Your brother, huh..."
    menu:
        "He should be more confident":# (+1 push Santiago)
            $ pushSanti +=1
            MainC "Honestly, he's got a good head on his shoulders."
            MainC "And he's nice enough."
            MainC "His confidence leaves something to be desired, though."
            Jock "Right?"
            Jock "And you saw him in front of the cameras. It's not like he can't be confident."
            MainC "What are you getting at?"
            "Gabriel ran a hand through his hair, clearly restless."
            Jock "I don't know. I don't know!"
            Jock "Something about it is ticking me off."
            Jock "He {i}can{/i} do things by himself. He should be able to."
            Jock "But you know why he won't?"
            MainC "Because you're there to help him?"
            Jock "Exactly."
            Jock "I was going to tell them to just take the bus here, you know?"
            Jock "There were tons of things I could be doing on a Friday night and none of them were this lame."
            Jock "But then I started worrying about him."
            MainC "It's natural to be worried. He's your family."
            "Gabriel's eyes avoided mine, anger simmering in his twisted sneer."
            Jock "That road should go both ways."
            Jock "When we get out of here he can just forget about asking me for anything ever again."
            Jock "Family or whatever, I'm done with it all."
            "Harsh words..."
        "He's too clingy.":# (-1 push Santiago)
            if pushSanti > 0:
                $ pushSanti -=1
            MainC "Hmm, how to put it."
            MainC "He has this vibe like he wouldn't be able to order a pizza on the phone."
            MainC "I'm assuming that's your job in the family unit."
            Jock "Bit harsh, don't you think?"
            MainC "You asked, I answered."
            Jock "..."
            "For the first time in our whole conversation, Gabriel stopped drumming his fingers against the wall."
            "His expression changed, too."
            "Before, his mouth had twisted in a way that made it look like he had bit into something particularly sour."
            "Then Gabriel sighed."
            Jock "I get what you mean. Sometimes I catch myself thinking stuff like that, too."
            Jock "Dunno if you've noticed, I have a bit of a temper."
            MainC "Color me shocked."
            Jock "Yeah, whatever."
            Jock "Santi is... he's trying, you know."
            Jock "This Gooptube stuff, he wouldn't have done that in a million years before."
            MainC "He was even shyer before?"
            "Gabriel threw his head back and cackled."
            Jock "Oh, you don't even know."
            Jock "Haah... I need to calm down."
            MainC "It looks like you worked something out."
            Jock "You know, I think I did."
            Jock "You should be a therapist or something."
            MainC "Funny."

