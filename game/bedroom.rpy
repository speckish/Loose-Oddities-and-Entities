scene hallway
"The door slowly opens with less of a fault of its own and more my own hesitance."
"I take one look at the room and shut the door again. "
"I blink. Once. Twice."
scene bedroom 
#note - floor
"I open the door to my mom's bedroom once more and confirm that no, I'm not hallucinating. It was hard to tell with the furniture worn and shoved haphazardly against the walls, but I could still make out the effeminate, childishly graceful designs. "
"My mom's childhood bedroom is princess themed. I didn't think she was the type. Then again, children don't really design their own rooms. Still, it was wholly unlike anything I would have imagined, especially considering she lived here until she was around eighteen."
scene bedroom
#note - pan up)
"Another thing wholly unlike I would have imagined was the cat-slug abomination hanging upside-down from the ceiling. It was… dripping? All the while swinging slightly side to side."
"Until it noticed me."
scene bedroom
#note - zoom in on Horned)
"It gave me the same double take I did."
h "Huh…?"
h "Now, who in the heck are you?"
h "Hello? I'm speaking to you? Did the old man send you up as a snack?"
menu:
"I'm Drew.":
    jump horn_intro
"You first.":
    jump horn_uno_reverse
"I'm here to dispose of you.":
    jump horn_dispose

label horn_dispose:
    d "I'm here to dispose of you."
    "She suddenly falls limp as if all the strength she had left in her body evaporated."
    h "Oh."
    h "Goody. Finally I will have an end to this hell."
    h "Well? Make it snappy. Get it over with all ready."

if with_cards:
    scene bedroom - zoom out + pan down)
    "A wiggle in my pocket snatches my attention. A card slips out, showing me a picture of escargot being seasoned with salt."
    "Before I can even comment about how specific that is, something thunks in the toy kitchen. I cautiously approach. I open the little wooden oven and stare at its contents, baffled."
    "I take out the tipped over carton of salt. It's honest to goodness real salt you use at the table and not the plastic knock-off version that comes with a kid's play kitchen."
    d "...I'm not going to question it."
    h "Hellooooo. Anticipation ain't doing it. Still here. Still. On the ceiling. Just swinging."
    scene bedroom 
    #note - pan up + zoom in to Horned)
    "I dump a handful out onto my palm and unceremoniously chuck it at h slug. She writhes. She shrieks. Her skin bubbles and melts."
    "And then she collapses into a puddle of goo on the floor, very much reminiscent of the Wicked Witch of the West."
    scene bedroom
    #note zoom out)
    "I'll mop it up later once everything is settled. If it stains the wood floors… it's not my fault."
    jump rooms_choice
else:
    d "Alright then. I'll try to make it quick."
    "I stab her with my kitchen knife. Yellow blood drips down the handle. It trickles over my fingers—"
    "I yank my hand back with a hiss and hastily wipe the blood off. I silently curse under my breath. Black veins steadily branch out over my skin where h creature's blood touches, burning ice and fire into my fingers."
    "Of course its blood would be poisonous, why wouldn't it be poisonous? Ugh. Hopefully this isn't permanent. And now my knife is coated in the stuff. How am I supposed to get it back now?"
    "The creature groans and shudders. "
    "Once. Twice."
    scene bedroom
    #note - zoom out)
    "And then she collapses into a puddle of goo, the blood and skin and whatever she was made of forming into one fluid. The knife bounces off the floor and lands a bit outside the perimeter."
    "I stare at the puddle and thoughtfully hum. "
    "Well… I'm not sure how I'm going to go about cleaning that. I might have to go out and grab some rubber gloves. That's a problem for later, though."
    jump rooms_choice

label horn_intro:
    d "“I'm Drew, the old man's granddaughter.”"
    h "“Oh. In that case, where's that insufferable geriatric then? Tell him I have a list of complaints I need to go through with him before I contemplate my existence at four today—”"

label horn_uno_reverse:
    d "You first."
    h "Do you not know who I am, maggot? I am the End, the Devourer of Worlds and Life, sent here to feast upon every mortal soul in this plane of existence!"
    "Yeah… I'm not going to call her all that."
    d "Alright, thanks for the introduction. I'm Drew."
    "She narrows her eyes at me and twists around."
    h "Drew? And what {i}drew{/i} you to this room, you insolent nonbeliever."
    h "Bring me that wrinkly older mortal, and he will confirm that I am indeed the ruler of gluttony unrivaled across all the cosmos—!”"
    d "He's dead."
    h "Oh."
    h "Huh."
    "She wiggles back and forth, and the hook in the top of the ceiling shudders with her movement. The practiced way she spoke falls away."
    h "Wonderful! Go and bring his body here so I can devour his corpse."
    d "His corpse is not in the house."
    h "Ugh! What a disappearment! Disappointment!"
    "The slip of her tongue doesn't stop her energy now that she has it."
    h "So, what are you? My new retainer? If so, can I have some suggestions, stipulations, sandwiches, and so on?"
    d "Sorry to disappoint…? But I'm only here to clean the house."
    h "Ah! You're the maid! If I must live in this hovel, it should be a nice respectable one. Clean it at once."
    d "I'm not—"
    h "Not the maid?"
    "She sucks in a deep breath and the wiggles desist."
    h "In that case, untie me, will you? I can't count the days I've been strung up like some common prey animal. It's utterly appalling for someone of my statue. Stature."
    if drew_kill_count > 0:
        "Honestly, letting go of someone who claims to be the harbinger of the apocalypse sounds like a highly irresponsible thing to do."
        "But then again, trying to get rid of her sounds like a hassle. And if I factor in all those razor sharp horns…"
        d "...Will you leave the house if I let you go?"
        h "With poor haste.{w=05} Or wait, that doesn't sound right? However that saying goes."
        d "Post. It's post haste."
        h "Well, chop chop, post girl. Get me down."
        d "Alright, hold still. I'll bring up a chair so I can reach you."
        jump minigame


scene bedroom
#note - pan down to floor)
h "Ah, to be free at last."
h "As thanks, I have magma—magazine—no. I have {i}magnanimously{/i} decided to spare your mortal soul when I eventually devour all Life in this universe."
d "...Okay then. Thanks."
h "It's your honor."
d "Thanks, your honor?"
h "What?"
d "What…?"
"We stare at each other for a beat."
d "I'm gonna… leave you to stretch out after being stuck up there for however long."
"I swiftly vacate the room. Sure, I might have unleashed the future harbinger of the apocalypse, but at least she'll be out of the house."
if rooms_left > 0:
    "I hope none of Grandpa's other “tenents” are this haughty. One is enough, thanks. "
else:
    "If Bedroom is the last room to be explored)"
"Am I ever glad she was the only one to be this haughty. Her personality at times vaguely reminds me of my mom. At least, that part of both of them that seemed made up."
jump rooms_choice
#(Minigame Info)
#note is this the mini game?
h "Oh… I wonder what I should do first out there. Oh! Oh! I know, I want to eat something sweet. Maybe one of those, uh… What's the word? It's sweet and slimy?"
menu:
    "Ice cream?":
    h "No, no, no! Cold things hurt my teeth!"
    "Sweetfish?":
    h "Yes! Raw, straight from the water into my gullet."
    "Jackfruit?":
    h "Who's Jack Fruit? …Is he delicious? Damn, now he's all I'm gonna be thinking about!"
h "Next, I'd like to dine on something fine. Like, uh, um… Sand? No, that's not it."
menu:
"Sandwiches?":
    h "Hm… Could go for a good bread on meat action anytime, but not what I'm thinking of. Come on, think better!"
"Dirt?":
    h "Nope. I ate that right before I got here, and I need variety in my life. What? You want me to live on a diet of {i}only{/i} decayed stuff? You're worse than gramps."
"A band full of hot people?":
    h "Yes! It's like you read my mind! Mmm, fresh musical meat. Sing me a ballad while you become my… meat salad."

h "…And then I think I'd top it off with something really good—something other people wouldn't dare to eat, you know? You know? What do you think you know? (The other two times were her forgetting the words, this time she's being playful on purpose.)"
menu:
    "Grandpa?":
    h "Mummy or ash, anything would be the best taste in the world. Silly little slugs like you are afraid of that forbidden meal, though. Heh. More for the All-Encompassing Me."
    "Yourself?":
    h "…People shouldn't even try, duh. But are you stupid? Why would I eat myself?"
    "Cockroaches?":
    h "Why shouldn't people eat cockroaches? Huh, you don't eat cockroaches? Why?"