label basement:
    "As I descend the stairs, I glide my hand against the wall and feel for a light switch. I find it after a moment and flick it on."
    "Of course, I brace myself for the worst."
    "The basement is emptier than I expected. There is some junk in a cart and a few boxes, but the clutter is nothing compared to what I've seen in other rooms."
    "In the center of the room, though, I see a woman standing and looking down at the floor. She slowly brings her head up and peeks through her long hair. As she moves, the ringing sound of metal on metal draws my attention to the chains that limit her movement."
    w "You—who are you?"
    d "Well, I'm cleaning the house for—"
    w "Let me go!"
    "The sudden rawness in her voice catches me off guard. She strains against the chains, trying to reach out for me. "
    d "Wait, just wait a moment—"
    w "Just let me go, please!"
    menu:
        "Question Her":
            jump question_her
        "Get Rid of Her":
            jump question_her
label question_her:
    d "Why are you locked up?"
    "She pauses for a moment."
    w "Well…"
    w "I am innocent, I swear! The man that lives here is cruel and locked me up to hurt me. I am nothing but innocent, just please let me go!"
    d "I don't know if someone that's innocent needs to say it so many times…"
    d "And I know the kinds of, um, powers that my grandfather dealt with."
    w "Grandfather?"
    "The woman tilts her head, and her expression of panic changes to one of curiosity. "
    d "Yeah, he's, well, dead."
    "Her eyes widen and her arms slump as much as they can in the chains. "
    w "Wow, I-I never would've guessed. He was old, but…"
    "The w  starts to laugh."
    w "I can't believe he finally kicked the bucket."
    d "Well, he did, and now I'm cleaning up."
    "I shift uncomfortably. The w  stares at me for a moment, before a smile forms on her face. She hums softly. "
    w "Maybe, if you let me go, I can give you something. Whatever you want. I'll give you anything."
    jump no_gotta_kill

label no_gotta_kill:
    d "Sorry, my mom told me to clean up. That includes you."
    w "Oh, oh no."
    "She recoils for a moment, a look of feigned fear on her face."
    d "Look, my grandfather died, I'm just trying to do—"
    w "Oh, so you're like him. "
    "The w  lunges at me, baring her teeth. Her eyes turn black as her lips curled into a smile."
    w "You know, sweetheart, I'm more powerful than you think. You can't kill me. I can't die."
    w "No matter what you do, I can find you. I will follow you wherever you go."
    "Her expression softens, and it calms my heart just a little. "
    w "If we come to an agreement, though, you can let me go. I can give you something. It's a win-win scenario."
    if choice_cards_01:
        "The cards flip to reveal a thinking face. Very helpful."
    menu:
        "Accept Bribe":
            jump accept_bribe
        "Deny the bribe":
            jump deny_bribe


label accept_bribe:
    "At least she's offering something other than death. "
    d "Okay, I'll do it. Just, is there anything I need to know so I don't hurt you?"
    w "Oh, just be quiet, sweetheart. "
    "She smiles, but it does nothing to calm my nerves. "
    "The w  doesn't move as I walk over to her. My hands shake as I reach up to unlock her bonds, but I manage to click the cuffs open."
    "Of course, she doesn't move the whole time. It's like she's trying to make the process difficult for me."
    "The w  stretches as she is released from her bonds, a wide grin on her face."
    w "Now, let's play a bit of a game, shall we?"
    d "What?"
    "It doesn't really seem like the time for games, but I'm not sure if I have much of a choice."
    w "You want your prize, don't you?"
    #MINIGAME GOES HERE
    if response == 'rude':
        if not minigame_win:
            "She walks towards me and places her hand on my shoulder."
            w  "In return, I'll give you a quick death."
            d  "Wait—"
            w  "You are too much like your grandfather. It's best for all of us. "
            "Her hair grows longer and her eyes go dark again. The next thing I know, there's something wrapped around my neck, tight enough to restrict my breathing. "
            "I reach up to try and pull it away from my neck, but my fingers only slip on the strange texture."
            "Then I realize that it's hair. "
            "There is hair wrapped around my neck and it's impossible to grip and as the long seconds tick by, my body starts to give up."
            "That's when I know there's no use struggling anymore. "
            "I go limp and the world goes dark."
        elif  minigame_win:
            "The w  huffs for a moment and crosses her arm like a child. "
            w "Well, I guess a deal's a deal, then."
            "She tilts her head."
            d "Will you head out, then?"
            w "If that's what pleases you, then sure."
            "She dramatically walks over to the stairs, before stopping on the bottom step."
    else:
        #(otherwise)
        #note so if player wasn't rude? 
        "The woman starts to laugh at me, a mischievous look in her eye."
        d "Are you alright?"
        w "Of course I am! It was fun to play with you."
        "She looks around for a moment, flexing her hands." 
        w "I never thought I would get out of here. Do you know how boring it is, being in this basement all of the time?"
        d "I guess it would be boring."
        "The woman  bounds over to me and pats my cheek."
        w "You know, you're quite endearing, sweetheart. I'll come up with something nice for you."
        d "Could you help me clean up the basement?"
        "The woman looks deep in thought for a moment."
        w "Well… no. It's probably more of a favor for me not to help."
        "The woman grins again and bounds over to the bottom step of the stairs."
w "I'll be upstairs, but I just have one more question."
d "I might be able to answer it."
w "Where's your grandpa now? Just the name of the graveyard is enough."
"A glint in her eye tells me she has a reason, but I don't press. "
"It'll be easier to just give her an answer."
menu:
    "He's been cremated":
        jump cremated
    "I'm not sure":
        jump omission
label cremated:
    d "He's actually in an urn now. My family cremated him. "
    "The w 's eyes light up."
    w "Oh, that's different. I like it."
    d "Just please don't mess with it."
    w "The urn's here?"
    "I don't answer that."
    w "Don't worry, I'll be good. I promise."
    "As she bounds up the stairs, I'm not entirely convinced."
label omission:
    d "Well, it's a little complicated. I'm not sure if the graveyard has a name at all."
    "Technically, it's not a lie, since I wouldn't say this house has a name to it."
    w "That would be something he would do, I guess."
    "She smiles and gives me a wave."
    w "I'll be upstairs, then. Feel free to visit."
    d "Don't break anything, please."
    "I don't want more messes to clean up. I'm probably not going to finish today as it is."
    w "I'll be good, don't worry."
    "As she bounds up the stairs, I'm not entirely convinced."
    if rooms_left > 0:
        "But now that she's gone, that's another room down. The basement isn't as bad as I first thought, but part of me wants to explore more before going through boxes and junk."
        "Who knows how many more of these strange inhabitants are around? "
    else:
        "Actually, this may be a good time to check on the living room. After all, I'm not too sure how well-acquainted these inhabitants are, and I would like to avoid fights if possible."
label deny_bribe:
    d "I don't know if I should take a bribe, but—"
    w "But you'll help me out of the kindness of your own heart?"
menu:
    "Help her out":
        jump help_her
    "Kill Her":
        jump kill_her

label help_her:
    "You know what, it can't hurt, right? "
    jump MINIGAME

label kill_her:
    d "Sorry, I have to. "
    "I pull out the knife. It's time to get rid of her. I'm not sure exactly what she did to end up here, but I need to clean this up. "
if choice_cards_01:
    "The cards rustle beside me, the faces quickly flipping between an assortment of images. Strangely, though, it's facing the woman instead of me. "
    w "Shut up, you little—"
    "She lunges forward and strains against her restraints. "
    jump straight_to_here
else:
    jump straight_to_here
#note is the cards section and additional snippnet before 'straight_to_here' ?

label straight_to_here:
    "I move quickly. After all, she can't really resist, and I don't want this to last too long. I walk up to her and put the knife up to her throat, slicing it in one motion."
    "Strangely, though, her solid body falls away. I blink a few times to be sure before I notice a pile of hair on the floor."
    "At least it'll be quicker to clean up."
if rooms_left > 0:
    "Now that the basement is done, I need to keep working. I may not finish this all in one day, but that doesn't mean I want to waste time."
else:
    "Well, I think the strangest of the work is done. Might as well head to the living room and take stock of what I still need to do."
    #note where does the story jump to from here?