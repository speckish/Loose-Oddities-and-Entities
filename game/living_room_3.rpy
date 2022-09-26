scene front_door
"After finishing a quick sweep of the rest of the house to make sure there are no more creepy creatures within these walls, hiding somewhere, I regroup onto the main floor."
"The walk to the living room feels weirder than when I first entered this place."
"First, it was all empty. And now…"
if people_still_alive:
    "It\'s anything, but."
else:
    "Even with fresh remains of something I thought didn\'t exist hours before decorating this house, that proved that there was a mystery to grandpa."
"One that I solved… in some ways worse than others."

scene living_room

"I step into the living room."

# flavor text for monsters
if last_monster == "orb":
    "Beside me, the orb rolls forward to join the rest."
elif last_monster == "mannequin" or last_monster == "doll":
    "A pile of worms carrying the cracked doll slithers forward from beside me."
elif last_monster == "woman":
    w "The woman saunters forward beside me, eyeing the doorway as we pass."
elif last_monster == "horned":
    h "The horned creature scampers forward faster than I thought she could walk."
if with_cards:
    "I feel the cards shuffle in my pocket."
elif cards_alive and not with_cards:
    "The cards are perked up on the mantle, looking at the newcomer and me. I wave. They shuffle and show me a door. Yeah, I\'ll get to it."
elif cards_killed:
    "My eyes immediately zone onto the mess the cards made earlier, and I tear my eyes away. That is a problem for later."

if last_monster == "Orb":
    #notes orb only?
    "It wheels into the living room, backs out to the entryway, and goes back in again."
    d "Must be happy that you can move around again, huh?"
    "It spins in a circle and settles in front of me, presumably just looking up at me as I look down."
    d "What?"
    "It rolls back out to the entryway. This time, I follow."

    scene front_door
    "It hovers around the outline of tape, rolling forward and back as if it\'s bouncing off an invisible forcefield."
    d "Oh, I got you."
    "I crouch down and start peeling the tape. The moment there is room for it to squeeze into the actual doorway, it pushes past me."
    "I stand and unlock the front door."
    d "Um. Good luck out there?"
    "It twirls once more and I pull the door open."
    "Without any fanfare, it zipped off, clunking down the porch steps, and wanders off into the world out of sight."
    d "Goodbye."
    jump to peace

(if Mannequin/Doll only):
#notes: monster selection?
    "A black wisp curls out of the doll, turning this way and that as if it was a telescope."
    doll "Wow.{w=0.5} It all looks as ugly as I remember."
    d "Can\'t say I don\'t disagree with you. But you won\'t have to look at it much longer."
    mann "We are free."
    d "Yeah, yeah, you are."
    doll "I want to explode."
    mann "We should regain our bearings."
    doll "Yeah, we\'ll do that. But I {i}want{/i} to explode."
    "I\'m not sure what that entails other than the obvious, and I hope it happens as far away as possible. I clap my hands together."
    d "I don\'t want to keep you from all that, so let me go free up the door."
    scene front_door    
    "I crouch in front of the door and begin to tear the tape up in chunks."
    doll "Maybe to stretch out, we can break into a library and throw things around. Pretend it\'s haunted."
    mann "That\'d be rude."
    "I nod despite myself."
    doll "Don\'t agree with him. Or do. It\'s not going to change my mind. Rude or not, it\'d be fun."
    mann "How about we break into a museum instead?"
    "How is that any different? I bite my tongue to stop it from speaking my thoughts, tearing off another piece with fervor."
    "Some of the glue sticks, but it\'s apparently okay because they slid right through before I\'m even finished with one section."
    "The worms stop in a pile right in front of the door and I shoo them to the side with my shoe—without touching, mind you. I\'m not interested in making a mistake right at the end."
    "I tug open the door and wave them through."
    doll "Freedom! Fresh air! Fuck yeah!"
    d "Enjoy it."
    "The worms always move faster than I think they will as they\'re nearly out before I\'m finished with my sentence. A clump near the back pauses, and a few worms look up at me."
    mann "…Thanks."
    d "No problem. Just… cleaning up."
    jump to peace

(if Woman only):
    "She walks around the room like she owns the place, poking at things here and there. She turns her nose up at the couch, flicks the iron fireguard, and then pauses."
    w "Is that painting new?"
    "She doesn\'t wait even a second for me to answer with a shrug. She purses her lips and spits on it."
    "Uh. Um, okay."
    "She turns to me, body language oozing with self-satisfaction."
    w "He had terrible interior decorating skills."
    w "And… where are the other little gremlins? I know he had others."
    w "Did you…"
    "She looks me up and down."
    w "Hm… Interesting. Very interesting."
    w "I\'ll keep that in mind."
    d "Why?"
    w "Well, I think you\'re just swell for letting me go, and I never forget a face. I\'ll be seeing you sometime or other."
    if omission:  
        #grandfather question in basement
        w "But first I need to visit your grandfather\'s grave, of course."
    if cremation:
        w "I\'m not going to leave his ashes alone forever, I hope you understand."
        "It takes all my willpower to not glance at his urn right behind her head."
        d "Yeah, okay."
        "I didn\'t agree to this on-going relationship, but if it gets her out of the house without causing a further mess, playing along works. "
        w "Open the door for me, will you?"
        "I nod and turn out of the room to do just that."
        scene front_door
        "It\'s not quick work pulling up the tape, and it feels even longer with her just standing there, staring at me with a widening smile every time I look up at her. This feels weird, right? This is weird."
        "With the final piece of tape removed off the floor, I make a sweeping gesture to the door. She looks at it, loops a finger through her bangs, and shakes her head."
        w "You need to untape the walls, too."
        d "Yeah, I don\'t think so."
        d "Are you sure?"
        w "One hundred percent."
        "I stare at the tape. It\'s a lot. Better get to work."
        "It\'s a good thirty minutes or more of me pulling tape off. I have to get a chair from the still stinking kitchen…and I\'m pretty sure she\'s staring at my ass. But I get it done and hop off the chair."
        "I open the door with a flourish, hoping she gets the hint."
        w "Thank you kindly. I\'ll be seeing you."
        "She winks at me."
        "And before I can blink, her skin is shifting into hair. She grabs the top of the door frame with it and slings herself up, out of sight. I lean away."
        jump to peace

if Horned only:
    "She looks around the empty living room."
    h "Huh, weren\'t there more of us? Or was I just special, trapped here all alone because I\'m so dangerous. He was so fearful of me for good reason."
    d "Yeah…"
    d "You want to wait here while I rip the tape off the door?"
    h "Oh, sure, sure! Absolutely. I\'m going to eat his dead couch. Or he\'s dead. Couch. I\'m gonna eat it."
    d "…Knock yourself out."
    h "Excuse me?"
    d "    Oh. It\'s, uh, a saying. It means: have fun."
    h "I see. I will."
    "She bounds straight into the couch and I twist away, walking back to the door. I don\'t want to see the process."
    scene front_door
    "I peel away a few layers of tape, enough for her to walk through."
    d "I\'m finished."
    "Her head peeps around the corner of the doorway. She smiles with all teeth—I can see a little bit of cloth and wood chips …and is that a staple?"
    h "Good! I had a snack for the road and I\'m ready to get on it and go! Far, far, {i}far{/i} away!"
    d "Glad to hear it."
    "I open the door and lean against it."
    h "…Thank you, peon. I\'ll not eat you if I ever see you out there."
    d "Glad to hear that, too."
    h "Heh. You should always count yourself lucky to be on my good side. Be more than glad, be ecstatic!"
    "She turns her head away, perhaps to be dramatic, but due to her anatomy, we just catch each other\'s eyes."
    "She nods once, then shescampers out the door and is out of sight before I know it."
    jump peace
else:
    "I turn to the collection of creatures and try not to feel like I\'m making a speech in some improv group."
    d "Okay, here we all are. Free."
    "I\'m met with blank stares."
if anyone is dead:
#note anyone not here?
    (if you have Woman):
        #note woman?
        w "Hm… Wait a minute. Is this all? I thought he was keeping more of us?"
    (elif you have Horned):
        "The horned one points to herself and then the person next to her."
        h "One, two…"
        h "Huh. I thought gramps had more."
        d "Um… Yeah, about that. I made some choices. Some actions."
    (if you have Doll):
        "The doll makes a weird snorting noise. I try not to react."
        d "And this is where we are, alright?"
    (if you have Woman):
        w "Hm? Alright."
    (elif you have Horned):
        h "Whatever."
    d "I\'m under the assumption none of you can leave since you haven\'t yet. So, I\'m going to untape the door. "
    "I pause, looking between them."
    d "No one kill each other. Or ruin anything in this house grievously, okay? I have enough cleaning work ahead of me. I don\'t want more."
(if you have Doll):
    d "Aye-aye."
(if you have Horned):
    h "Whatever"
(if you have Orb):
    "The orb rolls in a circle, then begins exploring the room."
(if you have Woman):
    w "So, what are you in here for? {i}Grievous{/i} actions against humanity?"
    "She\'s making fun of me, isn\'t she?"
    scene front_door
    "I listen with half an ear, but it\'s hard to follow any of the short, quiet discussions\' plot lines while the sound of tape ripping is happening by my own hands."
    "{i}Something something{/i} he\'s finally dead—{b}RIP!{/b}—{i}something{/i} hungry! And bored—{b}RIP!{/b}—what even are you—{b}RIP!{/b}"
    "When the ground is clear of tape and I make sure all the latches are indeed unlocked, I peek into the room. They\'re huddled in a circle as if they\'re in group therapy—a very self-interested type of group therapy."
(if you have Horned):
    "The horned creature is clearly chewing on something, and I can\'t tell what it is from a cursory glance around the room."
    d "I\'m finished."
(if you have Doll):
    d "\'Bout time!"
    "The pile of worms is still holding him in its lap. It perks up as well."
    "The group gathers at the front door."
if you have Horned: 
    h "It was nice meeting you, slug. Maybe I\'ll stop by sometime."
    h "Erm, hah! Scratch that. I don\'t ever want to set foot in this dump ever again."
    "Good thing since this place will be sold to some other person as soon as I get it presentable …{i}If{/i} I can get it presentable."
    h "But I promise I won\'t eat you if I see you out there. No promises about your friends or families or babies or pets."
    d "Okay. Good to know."
    "Actually, the opposite. The epitome of the opposite."
    h "Bye-bye!"
    "She skittered out the door before I or anyone else could scoot in another word."
(if you have Orb):
    "The orb rolled up and over the sill. I assume it\'s gonna wander off immediately—after all, the thing doesn\'t have a mouth to say goodbyes with. But it stops."
    "It turns around so the hat is pointed away from me, then rolls forward."
    "Did it… Is it tipping its hat at me?"
    "Huh."  
    "Okay. I nod back, hatless."
    "It spins on spot again and rolls away."

(if you have Woman):
    "The woman curls up beside me, her hair flicking at my cheek."
    "She hands me a slip of paper. It looks like it was ripped out of one of the magazines that was stacked up on a side table. There\'s a picture drawn on it with red ink…?"
    "Is this blood? Whose blood is it? Where did she get blood?!"
    d "Uh…"
    w "    If you need me, call me."
    w "    It\'s a favor I do not give lightly. Your grandfather may be the equivalent of a rotten carcass on a beach after several days, but you are no such thing."
    w "    He\'ll burn and you\'re rewarded for it. What a treat."
    "She waves to me with her hair and saunters out of the doorway. The moment she\'s outside, her form changes into her more monstrous one. She grabs onto a tree in the yard and pulls herself up and away."
    "I stuff the drawing in my pocket to ignore for now."

(if you have Mannequin/Doll):
    "The worm collective slither up by my feet. I look down at it and the doll it\'s carrying."
    doll "Hey, pipsqueak."
    "I\'m at least ten times bigger than him currently, but sure."
    doll "We wanted to say once again, thanks. Couldn\'t have done this without you."
    mann "A lesser person would have thrown us in a storage container and let it go to auction by never paying."
    d "That\'s really specific…"
    mann "I\'ve had plenty of time to think of what your grandfather\'s plan was."

    doll "And apparently, it was shit all."

    doll "And now I plan to do all the shit I couldn\'t while locked up in that box."

    mann "Anything and everything."

    d "I hope you two have fun."

    "And… don\'t hurt any people while doing it."
    "The doll gives me a final wave, and the worms carry him to freedom."

(#peace)
#note is this a label or jump?
"I close the door, press my hands against the wood, and just stand there for a moment."
"I reach up and clasp one of the locks before any second guessing happens and I have another infestation on my hands."
"Grandpa may have had all these locks and this tape to keep the monsters in, but I am a different person. Stay out."
"I turn around and begin to walk into the living room for a well-deserved rest."
"A muted scream down the block nearly makes me trip over my own feet. I readjust my stance, brush my shirt down as if it was covered in dust, and tell myself something."
d "Nope!"
"There was {i}no{/i} scream from down the street. There is {i}no{/i} reason to be nervous. I did my job, and I am not at fault if anything goes wrong. I am not a monster keeper. This is no longer my problem."
scene living_room
(if you have Cards):

"I look down at the last entity in the house: my companion for more than half of today\'s adventures, still in my pocket after all this."

d "How are you feeling about getting out there? I can…"

"I actually don\'t know what I can do for them. Huh."

"The cards shuffle quickly, thankfully breaking me out of the stumped silence."

"A stop sign. A mirror. A…puppy."

d "Charades have never been my forte, but I think I get it."

d "You want to stay?"

"A trophy."

d "Hm… If you promise not to make me mess up."

"They shuffle, stop, and start shuffling again. It takes a moment for them to show me their next card. The letters N-O."

"I snort despite myself."

d "Okay, point taken. Have it your way."

d "Speaking of your way, that can\'t be a card you have. That\'s too easy for a tarot set."

"The cards shuffle-laugh at me."

"I tuck them back in my pocket."

"(if Cards are alive, but not with you):"

"I turn back to the living room, looking for the last entity in the house. Those mischievous little cards."

    d "    Now, what do I do with you?"

    d "Can you… like, leave on your own, or do I need to bring you somewhere else? And if that\'s the case… "

"The cards shuffle through a few times before showing two cards—angel and money. Angel and money…? Uh, I guess."

d "A thrift store? Uh, no, I don\'t want to do that."

"The shuffling returns and then it slowly begins to lift what I can clearly make out is the boulder card."

d "Fine. Fine. Stop. You win."

d "…Just promise me you won\'t pick some kid to mess with? Find someone who melds with you?"

"A rhythmic shuffle—the laughing? Clapping?"

d "Good. Then, I\'ll drop you off somewhere once I finish here for the day."

"The cards quickly settle back onto the mantle. Silent."


"I drop onto the sofa and dig my phone out."

(if you have Woman):
    
"I momentarily pause my fingers when I notice a new red blotch on the couch\'s upholstery. My eyes fall down to the floor, and I see a marker halfway under the couch. "

"The symbol she drew me… It\'s just ink. Good to know."

"I return my focus to my phone."

"It\'s quick work dialing my mother\'s number, but it takes a second call for her to pick up this time."

m "What?"

"She\'s not facing the camera, and based on the sounds of the washing machine in the background, she\'s probably folding clothes."

d "I released them."

(If anyone is dead):
d "Well, some of them. But they\'re all …gone."

    (if you still have Cards):
"I can feel the cards shuffle in my pocket. I glance down and see a small face smiling at me. I look back up at the phone."

"Mom doesn\'t react for a moment, then she turns and gives me a look I hadn\'t seen on her before."

"It quickly turns into a pursed lip stare, and then everything falls away with a shrug. Apparently, she agrees with me. Not my problem, not her problem."

m "Dad shouldn\'t have been messing with all that. Just gives us more work."

"{i}Us{/i}? You didn\'t lift a finger."

m "I bet this is why he never invited us over. You know, I always thought it was because he was to cleaning like water is to oil. But, no."

d "No?"

"I am more than surprised. Mom hadn\'t been this vocal about him in over a decade. Even when we found out he died, she didn\'t have much to say."

m "No, he just kept doing the very thing I hated. And he lied about it. That was all he was interested in, you know? Those dreadful things? {i}All{/i} he wanted to talk about."
m "No time for little ol\' Beth. And when I clearly told him to stop keeping them, he apparently just stopped talking about them! That stupid man!"
"She grumbles something under her breath. Then, she glances back at the screen—at me—and blinks, her train of thought abruptly ending apparently. She sets her mouth straight."
m "Well, did you accomplish anything else?"
d "…I got the kitchen cleared out of food."
m "That\'s…"
"She gives me the eyeroll of a century."
m "Get back to it. You have no more distractions to stop you now."
d "Yeah, sure, mom. Thanks."
m "Don\'t give me that attitude."
m "…Call me when you\'re finishing up for the night. I\'ll order takeout."
d "Okay. Thanks, mom."
"She hangs up."
if Horned only:
"I lean back, only for something to loudly snap and I fall backwards, flinging my phone across the room. I lay in the mess that was once the couch for a long moment, regaining my bearings."
"I crawl my way off the pile and look at the wreckage."
"Ah. Orange slime."
"I forgot she said she was going to eat it."
else:
"I lean back into the couch, sinking into its worn-through padding. Until I hear something small crack inside, and push myself off before it breaks completely."
d "Goddammit, grandpa."
if with_cards:
    d "Or was it you?"
    I "look down at the cards and they shuffle quickly until the image of an angel is on top."
    d "    …Whatever."
    "I lightly kick the couch once, then walk out of the living room, stretching my hands over my head. The sooner I get this over with, the sooner I never have to deal with this house and its neglected insides ever again."
    "Maybe this time… I can actually start and {i}finish{/i} the office."
    (if you killed cards):
    "And as for the mess of plaster, planks, and an unnecessary amount of dust? Well, that seems like a job for a contractor. Not me."
    #After this, you unlock the notes grandfather had written about obtaining each one that are left in the office. THIS WILL ONLY BE WORKED ON IF WE HAVE TIME, but I plan to have them as a extra screen on the main menu. {Insert final line of game: Unlocked Notes!}
    return 
if not cards_alive:
    if len(monsters_dead) == 6:
        scene living_room
        "It\'s even emptier, somehow."
        "From the clumps of hairs that somehow are the remains of a woman in the basement, to the goo from the creature in my mom\'s old bedroom—well, they\'re all not alive anymore."
        "Gone is the curiosity I started with, and I\'m left with… nothing."
        "I stagger to the couch, in slow hulky movements, my body feeling off. I can\'t blame it after everything I\'ve gone through."
if cards_alive and not with_cards:
    "I throw a glance over to the mess made by the cards earlier. Just a huge pile of plaster and wood chunks right in front of the fireplace…"
    "I look away just as quickly."
    "Once I\'m sitting down, I tug my phone out of my pocket and call my mom. Twice, since she doesn\'t answer on the first ring."
    m "Wha—"
    d "It\'s done."
    m "…"
    m "What? What\'s done? You cleaned the entire house in less than a few hours?"
    d "…"
    d "No, mom. No."
    d "Those creatures—grandpa\'s hobby—I dealt with them. They\'re dead."
    m "…"
    "Her eyes surprisingly widen and gone is her usual aura of annoyance. She gives me a once-over, at least at the parts she can see and huffs out a breath through her nose."
    "Her mouth is still a frown, but it\'s different. She turns away as if catching on to the fact that I\'m surprised by her."
    m "Well, {i}good{/i}. Nothing to worry about now."
    m "He shouldn\'t have had any of those things anymore. I thought he wouldn\'t. He just…"
    m "He stopped talking about them, so I assumed he got over them. The same way he got over raising me."
    m "You know…"
    "She stops talking, so I prod her along with my usual “active listener” repertoire."
    d "Hm?"
    m " I think I would have preferred not to know he still had them. That he chose them over me."
    "She clears her throat. I think we both feel equally awkward. We\'ve never been the “talk about our sad kind of feelings” kind of family. Just the angry kind."
    "She won\'t meet my eyes or the camera when she continues."
    m "I bet you can finish quicker now that the hard part is out of the way. Go clean out the refrigerator."
    d "Already did that. Before all this."
    m "Then go clean the bathroom. I don\'t care. I\'ll order take out for dinner, so be home by seven."
    d "Okay. Sounds good."
    m "Good."
    "She hangs up."
    "I tuck my phone back into my pocket and sigh."
if with_cards:
    "I feel something move in my other pocket. Oh, yeah… The cards."
    "I pull them out, and it\'s showing a happy face on the top card. Glad one of us feels accomplished."
    "Hm…"
    menu:
        "Toss Them in the Fireplace":
            jump tossed
        "Keep Them":
            jump kept

label tossed:
    "I smile back."
    d "We should have celebratory drinks for a job well done, but I have nothing on me and neither does grandpa."
    d "Plus… I don\'t think you can drink? Liquid and cards don\'t mix. Probably?"
    "They don\'t answer."
    d "So, instead, how about a bonfire? We can relax in front of the fireplace for a bit and I will get to cleaning later."
    "They shuffle once and pull out a card."
    "Then another—an okay."
    "I stand up and grab the matches, getting to work to light the fire in the fireplace. The logs left there are so dry, it\'s barely a struggle."
    "Sitting down in front of it, I take the cards in my hand and show them it."
    d "It\'s been a long day for both of us, huh?"
    "They begin to move in my hands, but I grip them tight. I chuck them straight into the fire, watching the cards scatter in the heat, beginning to catch fire."
    "I sit there watching until every last trace of the twitching cards burns away."

label kept:
    "They might be a monster, but… While a little silly, they haven\'t harmed me, and even have been helpful."
    "Sure. Okay. They can stay."
    d "This isn\'t going to be so fun, but you can join me on my cleaning efforts."
    "They show a stick figure falling into a pond."
    d "Really? You\'re gonna make me slip on mop water or something?"
    "They shuffle for a long time. I assume they\'re laughing at me. Finally, they decide to show me a thumbs up."
    d "You know… You could make things easier for me, right? Why don\'t you do that?"
    "They\'re silent."
    d "Sadist."
    "Shuffling."
    "Only a few more hours and then I can pig out on whatever restaurant mom\'s picks—probably something a bit unhealthy but fulfilling. Just what I need."
    "I\'ll eat and then immediately go sleep off this day."
    "I get up, stretch, and get back to work."
(if Cards are alive, but not with you):
    #note
    "A shuffling noise happens behind me."
    "Ah, shit."
    "I turn around, already knowing what I was going to see. I forgot about the damn cards."
    "On top of the stack, one card is leaned up against the fireplace mantle. The image of a pit makes a pit grow in my stomach."
    "I hear a creak in the floorboards right beneath me, and then I am in a freefall."
    scene black   
    "I barely have a second to process before my back cracks against the basement floor and everything goes dark."
    scene cards_death
return
