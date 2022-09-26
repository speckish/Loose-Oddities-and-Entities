scene storage - on the left end + doll_chest
#note Expression:  Drew e, b, m
"I open the door to Grandpa's storage room, and the first thing that greets me is a box. On top of a box. On top of more boxes."
"Really, what was I expecting?"
#note Expression:  Drew e, b, m
"The thuds that I heard outside still continue as I glance around the room. I can't quite tell what's making the noise, but it's definitely in here somewhere."
"The amount of dust that kicks up as I step into the room sends me into an intense coughing fit, and I find myself stumbling over piles of random stuff to brace myself against a wall. "
if gone to OFFICE
#note Expression:  Drew e, b, m
"I can't decide which is worse: this place, or my grandpa's office. At least, when it comes to the dust."
if opened Orb
"The orb is a whole different story."
"I realize then that the scratching noise outside had stopped, which calms me a little. The last thing I need is for the orb to bust in and trap me in here. "
#note Expression:  Drew e, b, m
"I grab a box and open it up. Inside, there's mostly useless junk. A bunch of wires connected to nothing. A VHS Player that doesn't look like it's been used since before I was born. "
"Stuff that mom's going to want me to just throw out, most likely. "
"As I go to set the box to the side, a shiver runs down my spine. It's as if something is staring at me. But that couldn't be the case, right? Even with the thought of the strange orb still nagging at me, there couldn't be something else strange in this place, right?"
#note Expression:  Drew e, b, m
"Well, that's what I think, until I notice a figure staring at me from across the room."
if not gone to OFFICE
"This better not be what all the rooms are going to be like. I should have brought more water with me. "
"Well, better get working. The quicker I start, the quicker I can start getting to windows and opening them up. "
"I grab a box and open it up. Inside, there's mostly useless junk. A bunch of wires connected to nothing. A VHS Player that doesn't look like it's been used since before I was born. "
"Stuff that mom's going to want me to just throw out, most likely. "
"As I go to set the box to the side, a shiver runs down my spine. It's as if something is staring at me. But that couldn't be the case, right?"
"Well, that's what I think, until I notice a figure staring at me from across the room."
scene storage - pan to the right end
#note Expression:  Drew e, b, m
#note Expression:  Mannequin arm_down, en, mn
"It's some sort of mannequin. It only has the upper portion of its body, but I still scramble away from it. Its arms are more like drapes, slowly coming up as it continues to stare at me."
"And it's definitely staring. Even though it hasn't said anything, I can almost feel the life in its gaze."
menu: 
"The hell? #wtf "
"Interesting… #interesting"
jump to #wtf
#note Expression:  Drew e, b, m
d "What the hell was grandpa up to?"
???
 "Well, that's a little rude, isn't it?"
#note Expression:  Drew e, b, m
"I jump as I hear the soft, polite voice come from the mannequin. Its voice almost echoes for a moment in the room, and I can't help but shift uncomfortably."
#note Expression:  Drew e, b, m
d "Oh, I—you're really alive."
scene storage - zoom slightly into mannequin
#note Expression:  Drew e, b, m
"Despite the pounding in my heart, I move closer to the mannequin, terrified and enticed by it all at once. "
jump to #interesting
#note Expression:  Drew e, b, m
d "Interesting…"
"I gently move around the boxes, making sure not to disturb them too much and cause another dust-related coughing fit. There's a small clearing near where the mannequin is, and I stop there."
scene storage - zoom slightly into mannequin
"The mannequin tilts its head."
#note Expression:  Drew e, b, m
#note Expression:  Mannequin e, b, m
"???"
"You're not him. Who are you?"
"Before I can open my mouth to say anything, a thumping noise grabs my attention. For a moment, I freeze, until the mannequin lifts one of its arms and gestures to a chest sitting on the other side of the room. "
scene storage - zoom out and pan to the left, zoom into the chest
if gone to OFFICE
"The chest is wrapped in a ridiculously obnoxious yellow wrapping. An annoyingly familiar, obnoxious yellow wrapping. If it were anything else I would laugh, but given the strange orb that was covered in the yellow wrapping in the office, my heart just pounds harder."
"if not gone to OFFICE"
"The chest is wrapped in this strange, ridiculously obnoxious, yellow wrapping. I don't think I've ever seen anything like it before. And yet, I still hesitate to approach it."
scene storage - zoom out and pan to the right
"The mann "You should open that. "
d "I “should”?
"The mann "Yes."
"I'm not sure why, but it feels like a demand."
menu: 
Don't open the chest. #don't_open_it 
Open the chest. #open_it
jump to #don't_open_it
d "I'm not really sure, maybe I should wait—"
"I cut myself off as I notice one of the mannequin's arms move towards me. At first, I'm confused, until the fabric brushes against my neck."
"This isn't a demand anymore. This is a threat."
menu: 
Open the chest. #open_it 
Try to escape. #try_to_escape
jump to #open_it
jump to #try_to_escape
"My fight-or-flight instincts are completely in flight mode now. Before the mannequin can wrap its draping arm around my neck any further, I scramble away."
"Even when I'm out of the mannequin's grasp, I move as fast as I can, not caring about the boxes I knock over or the dust that I kick up."
"The mannequin can't even move. And yet here I am, running like I'm in a slasher film. "
"At least it gets me to the door."
scene hallway
if Orb is in Hallway
"I don't even bother to check my surroundings as I stumble out to the hallway. Big mistake. "
"Just moments after the door clicks shut behind me, my foot knocks into something solid. "
"The pain that comes soon after reminds me of the orb that I let wander the hallway. "
"I watch a blur of darkness retract back into the orb, and my legs give out underneath me."
"Collapsed on the floor, the last thing I see before everything goes dark is the orb beside me."
"Funny, even without a face, it looks sorry."
return
if not gone to OFFICE
"Well, I'm not quite sure if I want to continue cleaning that room."
"Maybe the office will give me better luck. I hope so."
jump to #office_1
if gone to OFFICE but did not release Orb
"Okay, there are some things that definitely need to be explained to me. Mom may not know exactly what's going on, but maybe she can give me some advice."
"After all, there seem to be some things here that I can't just sweep away with a broom. "
"I know the living room is calm, though. Somewhere that this strange mannequin can't follow and there aren't any other strange things that could kill me."
"I'll call Mom there."
jump to #open_it
d "Okay, I'll do it."
scene storage - pan to the left, zoom into the chest
"I kneel next to it, placing a hand on top until it stops shuddering as violently.  I peek up to the mannequin to make sure I'm still okay to open the chest, and a nod gives me my answer."
"The wrapping is thick and difficult to get off, but after a few horribly embarrassing moments, I manage to get the chest open."
scene storage + Close Up on Doll
"Inside of the chest is a little clown-like doll. It looks up at me and begins to shudder again."
"Poor thing. It looks like a pathetic puppy sitting there in the chest."
menu: 
    "Grab the doll.":
        jump grab_it 
    "Don't grab the doll.":
        jump dont_grab_it
label grab_it:
    "It is too much for me to bear. I reach down and gently scoop up the little doll. Hopefully I don't scare it too much."
    "The screams in my head tell me that I failed."
    mann "Wait—"
    "The mannequin sighs when it realizes its warning was too late. "
    "Even as I drop the doll back into the chest, the screams continue. My vision blurs and something wet begins to drip down from my nose. "
    "I collapse against the mannequin and the last thing I sense before everything goes dark is the brush of the mannequin's fabric arm against my cheek."
    scene doll_death
    return
label dont_grab_it:
scene storage - zoom out, Mannequin is closer
"I look up at the mannequin. I'm guessing that it knows much more than I do about this doll, and I don't want to scare the little thing."
mann "Don't touch it."
"It brings its fabric arm down to scoop up the doll. The doll begins to calm down as it is brought up to the mannequin's shoulder. "
d "Is it okay?"
"The mannequin doesn't answer me. "
d "Do you need anything?"
"Something tells me to try and be helpful to these two, but the mannequin seems preoccupied with the doll. It mumbles to the silent doll on its shoulder and pats it softly with its arm."
"I think it's time for me to go."
"I stand up quietly and move towards the door. It creaks as I open it, but neither the mannequin nor the doll look at me as I slip out."
scene hallway
if "office" in rooms_explored:
    "I think it's time for me to call mom. She better have some good explanations for this."
if ball in Hallway
    "I make sure to stay away from the orb that I accidentally let out before I head down the stairs and back to the living room."
    jump Living_Room_2
if not gone to OFFICE
    "Now that the two of them seem settled, I decide that it's time to tackle another room."
    "There's that office I saw before. Maybe I'll go there for now."
    jump to office
