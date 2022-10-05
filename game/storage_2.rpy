scene hallway
if orb_unwrapped:
    "As I get to the top of the stairs, I keep an eye out for the little orb rolling around the hallway. It may look harmless, and almost a little cute, but I think it's for the best if I stay out of its way."
    "The storage room. It's best if I go in and get this over with. Hopefully the dust doesn't kill me before I figure this all out."
if not open_doll_chest:
    scene storage
    "The door creaks when I open it, and I know the mannequin on the other side of the room immediately knows of my presence. Though the heavy thuds and shudders coming from the chest by its side may have masked the noise a little."
else:
    scene storage
    #note zoom in to Mannequin
    "mann Have you changed your mind?"
    "Its voice is steady and patient, as if it's prepared for me to bolt again. "
    "But I won't. I want to get this house cleaned before dark, and I'm not letting an angry box get in my way."
    menu:
        "Yes.":
            jump yes
        "Not yet.":
            jump not_yet

label yes:
    d "Yeah, sorry about that."
    mann "You are easily frightened."
    "Is it making fun of me? I can't tell from the even, almost deadpan tone that comes from the mannequin at all times. It shouldn't matter, though."
    scene storage
    #note - zoom down to chest
    "I walk over to the box next to the mannequin and kneel down, wary of the fabric arm that dangles next to me. "
    scene storage
    #note - + Close Up of Doll
    "When I rip the wrapping off and manage to open the box, the arm doesn't wrap around me. Instead, it picks up a shuddering, clown-like doll that had been trapped in the box, placing the little thing on the mannequin's shoulder. "
    scene storage
    #note - hide Close Up of Doll + pan to Mannequin+Doll
    d "Hey there, little guy."
    "The doll calms down as it sits on the mannequin's shoulder. After a few moments, it gives me a wave."
    mann "You should touch the doll."
    d "What?"
    mann "It's complicated to explain. Just do it. He's not going to hurt you."
    menu:
        "No thanks.":
            jump no_thank
        "Okay.":
            jump okay

label not_yet:
d "First, I just want to know, what exactly is in the box?"
scene storage
#note - zoom down to chest
"With the amount that the box is shuddering, I'm pretty sure whatever is inside is going to fling itself out at me."
scene storage
#note - zoom in to mann Mannequin
"I guess that is fair. My apologies."
mann "My friend is trapped inside of there. He's scared. If you could let him out, that would be very helpful."
d "Okay…"
"I have the information. Now it's time to actually make a decision."
menu:
    "Okay.":
        jump yes
    "No way.": 
        jump attack
jump to #yes
jump to #attack
#note - is this 'yes' or 'attack'?
d "I'm sorry, but I can't."
mann "What?"
"I pull out the knife without another word. The mannequin's expression doesn't change, but then again, I'm not even sure if its expression can change. "
if with_cards:
    "Either way, the cards aren't warning me about the mannequin, and as I slice through the fabric on its chest, the mannequin doesn't even begin to fight back."
else:
    "Either way, when I slice through the fabric on the mannequin's chest, it doesn't even try to fight back. "
#both
#note - what is 'both' ?
"This is going to be a painfully easy fight, isn't it?"
"Inside of the mannequin is a bundle of what at first look like wires. They writhe at the wound, a few even trying to grip the fabric to pull it back together. That's when I realize: those are worms."
"Some very, very strange kind of worms."
"There is a thicker mass at the center of them, almost like a heart. Bullseye."
mann "Oh, I see."
"I grab the shoulder of the mannequin to brace myself before I plunge the knife into the thicker mass. The mannequin jolts for a moment, before the fabric body goes limp and the bundle of worms flops onto the floor."
scene storage
#note - zoom out
"Dead."
scene storage
#note - zoom in to chest
"The chest starts to make even more noise once that happens, as if whatever is inside knows exactly what happened."
"It's probably best not to open that now, because the mannequin's friend is probably incredibly angry. "
"There was a fireplace in the living room, right? Best to dispose of it there."
#jump to rooms_choice
if open_doll_chest:
    scene storage
    "As I walk in, the mannequin and the doll look over at me, and the doll waves at me with its small hand."
    scene storage
    #note - zoom in to Mannequin+Doll
    mann "You're back."
    d "Well, I'm supposed to be cleaning all of this up."
    "I gesture around to the piles of boxes that still surround the room. The mannequin gives a disappointed hum."
    mann "I don't believe it will be of much use."
    "The doll pokes the mannequin's face and waves its arms frantically. "
    mann "Oh, of course."
    mann "Could you touch the doll? I promise it won't hurt."
    "I'm confused, but I have a feeling the mannequin isn't going to give much more of an explanation."
    menu: 
        "No thank you.":
            jump no_thanks
        "Okay.":
            jump okay

label no_thanks:
d "I think touching things just leads to bad things here."
"The doll isn't too pleased. It slams its hands against the mannequin's shoulder like a child having a tantrum until the mannequin pats its head with a fabric arm."
mann "I guess that is fair. It just wants to know who you are."

label okay:
    "The mannequin hasn't steered me wrong yet, right? I step forward and pat the doll on the head."
    "At first, nothing changes."
    mann "Just wait a moment."
    "My brain begins to feel fuzzy, but not in a way that makes me think I'm about to die. It's almost comforting, in a really strange way."
    "Even stranger is the voice that cuts clearly through the fuzz."
    d "Howdy there!"
    "I blink quickly, glancing between the doll and the mannequin."
    d "It's me, you idiot. The doll."
    d "Who the hell are you?"
    d "Oh, I'm not my grandfather, if that's what you're asking."
    if touched_doll:
        "The doll's voice pops into my mind."
        d "Well, obviously. He's old. And you're not."
        "Is that supposed to be a compliment?"
        "either"
        d "He's, uh, dead actually. "
        mann "Surprised he made it this long."
        d "Yeah, uh, I'm just here to clean out the house."
        d "So…"
        menu: 
            "Let them go.":
                jump let_them_go 
            "Dispose of them.":
                jump dispose_of_them
label let_them_go:
if len(dead_characters) > 0:
    "They seem nice. While grandfather may have had good reasons for keeping the others under lock and key, these two deserve to go free."
    d "You can head out of here, if you want."
    "The two of them look at me for a moment, completely silent."
    d "Like, I don't want to be rude and kick you both out, but it would be best if you would leave."
    "They stay silent, until the doll suddenly lets out a loud whoop. "
    "I jump at the noise, not expecting the doll to make a noise. "
    if touched_doll:
        "The doll's voice cuts through my mind again."
        d "We're free? Are you freeing us?"
        d "I guess I am."
        "either"
        mann "Thank you."
        d "It's not really anything. "
        "I look at the two of them for a moment, particularly the stand that serves as a very useless leg for the mannequin."
        d "Are you able to get out of here on your own, or…?"
        mann "Actually, if you could, I need help being released from my bonds."
        "I'm confused, but the mannequin turns around. There are two long strips of tape running down its back."
    #NOTE INSERT MINI GAME
    # MINIGAME
    if minigame_win:
        "I look down at the pile of worms that is now on the floor before my attention is drawn back to the doll."
        d "Are you good?"
        if touched_doll:
            d "Actually, there's a hammer nearby. Somewhere. Get it."
            d "And what am I doing with that?"
            d "Smash me."
            d "What?"
            "Logic tells me that would kill the doll that I'm trying to be nice to."
            d "Oh, I'll be fine. Don't worry."
            "I go through a few boxes until I find the hammer, the doll being entirely unhelpful during the process."
            "Then, I turn back to him."
        else:
            mann "Get the hammer out of this box. "
            "One of the worms reaches out of the pile and taps one of the boxes."
            d "And what am I doing with it, exactly?"
            mann "You have to break the ceramic shell. It won't hurt him, but he's a little trapped in there right now."
            "I glance over at the doll, who gives what I have to call a nod."
            d "Okay. Tell me if I'm being too rough though."
            mann "You won't be too rough."
            "I fish the hammer out of the box before turning back to the doll."
            "He looks about as ready as one can be to have themselves smashed by a hammer."
        #NOTE INSERT MINI GAME
        # MINIGAME
    if minigame_status == "win":
        "The doll is thoroughly cracked, with a weird dark mist drifting out of him."
        "For a few seconds, I think I fucked up, and glance down at the pile of worms for some sort of reassurance."
        mann "Just wait."
        "Just as he says that, the dark mist bursts out from the doll and takes a more solid humanoid form."
        d "Finally!"
        "The doll whoops for joy, before abruptly stopping."
        "He looks down at himself, and even though he doesn't have the most obvious facial expressions, he looks disappointed."
        d "I remember this being more thrilling."
        d "Huh? It looks cool to me."
        d "No, it's not-shit, I'm going to try that again later."
        "The doll's form begins to dissipate into mist again."
        d "Wait-"
        mann "Just let him be, he's being dramatic."
        d "No I'm not! This just wasn't the spectacle that it was supposed to be."
        mann "My point stands."
if not touched doll
"The doll looks at me, as if really noticing me for the first time."
d "Howdy, by the way. How are you?"
d "Well, I guess-"
d "Actually, I don't care. Bye."
"The mannequin sighs."
"end split"
"The doll's shadowy form sinks back into its now cracked ceramic shell without another word like a turtle hiding in its shell."
"I open my mouth to say something, but decide against it."
"The pile of worms reaches up to scoop the doll and bring him down. The doll settles himself on the top of the pile like a cowboy on a horse before waving up to me."
mann "See you around."
d "Be safe."
"I give the two a wave as they slither out of the room. The storage room is still full of dusty junk, but I'm not too worried about it."
if rooms_left >0:
    "I should go check to see if there are any other strange residents that I need to deal with."
    jump rooms_choice
else:
    "Maybe I should go down to the living room and check on everyone. Mostly to make sure they didn't all wreck the entire downstairs while I was busy."
    jump dispose_of_them
d "I'm sorry. I need to do this."
"I pull out the knife and take a deep breath. If mom says I need to do this, I guess I have to."
if len(characters_saved) > 0:
    "While they seem polite, something is off about these two. I don't think it's wise to keep them around."
    mann "No you don't."
    d "Yes I do."
    "I raise the knife up and take a step closer to the two."
    if touched_doll:
        "Before I can attack, though, my vision goes white. The fuzz enters my mind again, but this time it's angrier. More violent."
        "I drop the knife and my heart begins to beat faster. The doll is screaming expletives into my mind. Even though the noise doesn't even form into real words, I just know."
        "I don't remember collapsing, but when my vision starts to return, I'm looking at the ceiling. Not like the sight lasts long. My vision fills with every color and no color all at once, and every nerve in my body fills with the kind of pain that makes everything go numb."
        "And then the world goes black."
        return
    else:
    "The doll reaches out for me, but the mannequin picks him up and holds him far away from me. My knife reaches the mannequin first, slashing at its fabric body."
        if with_cards:
            "A few of the cards drop on the floor. An image of a doll, a hand, and a stop sign. "
            "Somehow, I understand that it won't be smart to let this doll touch me."
            "Unfortunately, though, the mannequin seems to know this. The next thing I know, the doll is being thrown at me. "
            "The cards ruffle in front of me, knocking the doll back into the chest. "
            "I don't hesitate. "
            "Before the mannequin can reach for the doll again, I plunge the knife into his chest. The fabric rips, and strange worms lash at my arm. I push deeper and hit something solid."
            "With one more push, the mannequin goes limp."
            "The doll is furious now, scrambling to get back out of the chest. Before it can, I rush over and slam the lid shut, using some of the tape I had ripped off to seal it back up."
            "There's a fireplace in the living room. Maybe that will work."
        else:
        "I don't hesitate. "
        "I slash at the mannequin's arm before he can react again, letting the doll tumble back into the chest. Before the mannequin can move to pick up and protect the doll again, I shove him against the wall and plunge my knife into his chest."
        "For a moment, the mannequin squirms. Strange worms writhed from the hole in his chest, weakly lashing out at my hand. The knife hit a thick mass in the core of the mannequin, which resists its point for a moment before giving in."
        "The mannequin goes limp."
        "As I pull out the knife from the mannequin, I notice the doll struggle to get out of the chest. I rush over and slam the chest before he can manage to get out. Some of the tape from the chest is still nearby, and I use it to keep the chest shut. "
        "There's a fireplace in the living room. That should work to get rid of this."
    $ rooms_left = rooms_left - 1
    jump rooms_choice
