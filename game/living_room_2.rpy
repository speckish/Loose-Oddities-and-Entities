scene living_room 
"I tumble into the living room and collapse on the sofa, panting heavily. "
d "Screw this."
"I push myself off the couch with a scowl and dig through my bag, whipping out my phone. "
"It rings once. Twice. "
"Click. Her face fills the screen."
m "Oh. It's you."
m "Have you finished even one room yet? If not, why are you calling me?"
"I internally sigh. Not five seconds in and I'm already exhausted. "
d "Hello to you too, Mom."
d "Say, did Grandpa… keep anything weird?"
"She squinted at me for a moment before something clicked in her eyes."
m "Seriously…?"
m "{i}God{/i}damnit, dad."
d "So you do know what's going on."
m "Barely."
"She swirled her hand, non-committedly."
m "Just throw whatever you find out into the trash. I'm sure they're… contained or something."
"She spit out the word they're."
m "Right? They're contained?"
"I open my mouth. I close it and shrug."
d "Maybe?"
"Something fiercer burns in her. I don't know where it's coming from."
m "They better goddamn well be."
m "And get rid of them. He should have gotten rid of them."
m "I don't want them anywhere near the house, you got that?"
menu:
    "I can handle it.":
        $card_liked_that += 1
        jump pacifist_route
    "…Yeah, sure… ":
        jump pacifist_route
label genocide_route:
    d "I will, so don't worry about it. I'll get rid of them."
    m "Good."

label pacifist_route:
    "I open my mouth, but leave it hanging for a moment too long. Her brows form a deeper wrinkle in her forehead."
    d "Yeah, sure… But, what—"
    m "But nothing. Those things have no business being in the house, so get rid of them."
    d "...Yeah."
    m "Good. Now get back to cleaning."
    d "Right. Bye."
    "Click."
    "I sag into the cushions with a sigh and a metaphorical sledgehammer pounding my head. "
    "Ah, yes. Nothing like a migraine when you have a full day's work ahead of you. How lovely. "
    "I push off the sofa with a grunt. I pace the length of the living room, rubbing my temples, trying to stave off the headache to little success. "
    "Ugh, this is going nowhere. I need a distraction to take my mind off of things. "
    "I pause. Oh, that's convenient. I see a pack of tarot cards on the mantle."
    scene living_room
    #note zoom into fireplace mantle
    "I pick them up and begin shuffling through them. My old college roommate used to read my fortune all the time with these. The last reading I did with her said my career would be a success. "
    "And yet here I am, five years later after working at a dead end job, in between jobs. How accurate. "
    scene living_room
    #note + Close Up for Cards
    "I flip over a card and frown. Since when do tarot sets include depictions of people tripping over rocks?"
    scene living_room
    #note hide close up and zoom out
    "I set the deck down with a huff and turn away. "
    "Thwack. "
    "I suck in a deep breath and keel over, grabbing my throbbing toe. I glare at the offending coffee table. "
    d "Son of a—"
    "I hear a shuffle. I glance back and freeze. "
    "Oh. Should've known. "
    scene living_room
    #note zoom in to fireplace mantle + Close Up for Cards
    "The deck of tarot cards hovered above the mantle, slapping on a giggling face. "
    "No, really. It drew a card with a giggling face on it and slapped it on top. "
    "I take a sharp, quick breath in. What should I do?"
    "A breath out. It's obvious. I should…"
    menu:
        "Negotiate":
            jump cards_talk
        "Burn it" : 
            jump cards_burn

label cards_talk:
d "Look, I'm not my grandpa or whoever it was that locked you up. So whatever beef you have with them, leave it, because I don't have the same history they do with you."
"The cards slap on a new face. It was the most unimpressed 'duh' I have ever seen on a 2D cardstock surface, and it gestures to the urn beside it housing Grandpa's ashes."
"A brow shot up to my forehead."
d "So... I take it you've been watching me then if you already know about that."
"A new card slaps on top. It wasn't an expression, but a depiction of a shattered mirror this time. "
"I wonder why—?"
scene living_room
#note hide Close Up for Cards
"The urn slides off the mantle. My heart leaps to my throat. Before I could think twice, I—"
menu:
    "Grab the urn":
        jump cards_convince
    "Grab the matches":
        jump cards_threaten
label cards_convince:
"—dive for the save of the century (literally, considering Grandpa lived to be a century old. I tumble and pop back to my feet, urn intact and in my hands. "
scene living_room -
#note Close Up for Cards
"I glare at the cards. It slaps on a smiley face. "
"I glare harder."
"Its smiley face turns into a sad face, complete with a comical tear running down its face. "
d "Look, I'm not... I'm not here to hurt you. I'm here to clean up the house. I have no problems letting you go as long as you don't cause me any trouble. So what do you say? Truce?"
"It stills, contemplating. Then it shuffles its deck and flops onto the mantle."
#note insert minigame
# Minigame time
if minigame_status == "lose":
    "I blink. It's the same card as before."
    if card_liked_that > 0:
        "The cards quickly shuffle and show me a crying face."
    else:
        "They shuffle hurriedly, in a rhythm that could be similar to laughing."
        d "What?"
        "There is a snapping noise and then the mirror hanging over the mantle falls straight at me. It slams into my head and shatters."
        "Everything goes dark."
        scene cards_death
        return 
elif minigame_status == "neutral":
    "I stare at the card I picked. It's just an unamused face."
    d "Okay?"
    "I blink and the tongue is now sticking out. Or was it always? Huh…?"
    "I put it back down on the mantle with the rest of the cards. The cards pile back up shortly and shuffle themselves, slowly."
    jump comewith

elif minigame_status == "win":
    if card_liked_that <= 0:
        "The cards still for a moment and then shuffle themselves slowly. They pull out a card."
        "A trophy."
        jump comewith
    elif card_liked_that > 0:
        "I draw a card and raise a brow at the depiction, baffled. This is..."
    menu:
        "Disgusting":
            jump cards_ew
        "Makes Absolutely No Amount of Sense":
            jump cards_idk
label cards_ew:
    d "Gross. Why would you show me this?"
    "It pauses and tilts, considering."
    "It draws a new card. I stare at it for a second, confused. "
    "What does a bunch of boulders falling have anything to do with—?"
    "A creak. A crack. "
    "I glance up right as the ceiling comes down on my head, crushing me dead under ten tons of plaster and wood."
    scene cards_death
    return

label cards_idk:
    d "... I'm not sure how to interpret that, so I won't."
    "The cards twirl in the air. I'll assume that means my bafflement brings it joy, which probably means I'll wind up with many more migraines before the day is done.  "
    d "So why weren't you taped up like the others?"
    "It flips through a circuit of cards. Somehow, by some miracle, I'm able to decipher what it's saying."
    d "Ah. As long as no one comes close or touches you, then you remain inert?"
    "It slaps on a thumbs up. "
    d "Alright then. You wouldn't happen to know about the other residents in the house, aside from the ones in the office and storage rooms?"
    "Two cards flick out and land on the mantle. I draw closer, inspecting them."
    "One houses a depiction of a lady with enough hair to give Rapunzel a run for her nonexistent money, while the other was... um. . . something that looks like a slimy caterpillar in a chrysalis."
    d "Thanks for the info. I'll come back for you when I'm—"
    scene living_room
    #note hide Close Up for Cards
#notes (Add Screen of Cards on the textbox
label comewith:
    "It zips and burrows itself into my jacket pocket. I blink, owl-eyed."
    d "... Okay then. You can come with me."
    "The card with the thumbs up peeks from my pocket. I sure hope I don't live to regret this. Or die, regretting it."
    d "Let's get going then, we have a house to clean."
    $ rooms_left = rooms_left - 1
    jump rooms_choice
label cards_threaten:
    "—grab the matches and brandish them. "
    scene living_room
    #note Close Up for Cards
    "The urn stops. The cards stops."
    d "I may not like the old man either. Hell, I don't really even know him."
    d "But I can't have you messing with his ashes and making an even bigger mess for me to clean. So why don't you put the urn back where it was, and I'll do the same with the matches?"
    "It quivers. "
    scene living_room
    #note hide Close Up for Cards
    "Eventually, the urn begrudgingly inches back to its rightful place, and I set the box of matches to the side. I could practically feel the card deck's glower on me."
    "I shrug."
    d "Sorry, but it's nothing personal."
    scene living_room
    #note zoom out
    "It whirls around, making it clear that it thinks that it very much is personal. I shake my head with a sigh and leave the room. "
    "I grunt as my shirt got caught. "
    "I glance down to see the material snagged on a doorknob. "
    d "Oh, real mature."
    "The cards shuffle and flip me a mirthful laugh. "
    "Whatever. At least that one is down. "
    $ rooms_left = rooms_left - 1
    jump rooms_choice
label cards_burn:
"My eyes dart to the matches on the mantle and the kindling in the fireplace. The cards still."
scene living_room
#note Close Up for Cards
"It swiftly flips to a depiction of raining arrows and rockets a volley of fire pokers my way. I duck and snatch the matches, popping open the box and striking a flare. The pokers round back. I swerve and barely avoid a skewering, but the cards weren't done dealing with me yet. "
"It flips to a picture of falling boulders. "
scene living_room
#note zoom out + hide Close Up for Cards
"The support beams over my head groan. Wood dust and bits of plaster trickle down. "
"The part of the ceiling right above me caves in with a thunderous roar right as I grab the set of cards and set it alight. It catches fire. It thrashes in my grip, panicked."
"I toss it into the fireplace just as the plaster and wood drop on top of me. "
"Silence."
"I cough as I crawl out of the rubble. I'm aching everywhere, but a quick count told me I have all my fingers and toes intact. "
"The fire burned merrily in the fireplace. I watch as the cards blacken and turn to soot. "
"I dust myself off with a sigh. Well, that's one oddity down."
jump rooms_choice

label rooms_choice:
"I'll head to…"
menu:
    "I'll head to..."
    "office" if not office_explored:
        jump office_2
    "storage" if not storage_explored:
        jump storage_2
    "basement" if not basement_explored:
        jump basement
    "bedroom" if not bedroom_explored:
        jump bedroom
#(After they are played, the choice disappears the next time we visit this menu.
#(Once they are all played, (#jump to living_room_3
