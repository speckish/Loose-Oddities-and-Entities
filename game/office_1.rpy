scene: office + bg_orb)
#note- Expression: Drew ecs, mf)
"The door to the office creaks as I twist the ancient, tarnished handle and allow fresh air into the room."
#note- Expression: Drew ec, mg)
"I cough out stale air and dust. "
#note- Expression: Drew enf, bn, mf)
"Ugh. The word \"musty\" doesn't cover half of it. And don't get me started on the mess. An upended typewriter, a shelf of random junk, some kind of list on the desk with a third of its contents hastily scratched out, and as for the cabinet—"
#note- Expression: Drew ecs, bh, mg)
"The drawer shuffles out with an ear-grating screech. I grit my teeth but soldier on, taking inventory. "
#note- Expression: Drew enf, bh, mn)
"It's half empty, and the other half is bursting with files haphazardly organized. Grandpa was really living the bachelor life here, huh?"
#note- Expression: Drew ec, bw, msh)
"I sigh, pressing my fingers to my temples. Alright, first things first. Time to clear out that shelf. "
#note- Expression: Drew enf, bn, mf)
"I grab a nearby basket and unceremoniously sweep junk inside, systematically dumping level by level. I can't tell what half of this stuff even is. Case and point—this garishly wrapped bowling ball. "
scene office - zoom into orb
If gone to STORAGE first
#note- Expression: Drew ecf, bh, msh)
"I pause. "
#note- Expression: Drew bw)
"Wait, I've seen this hideous wrapping before. Wasn't this on the chest in the Storage room with the talking mannequin? Is this another one of Grandpa's \"surprises\”?"
"I warily eye the deceptively innocent-seeming bowling ball. "
(If not gone to STORAGE yet)
#note- Expression: Drew ecf, bh, mf)
"Who giftwraps a bowling ball in tape with the most eye-watering shade of yellow imaginable? It's like its very existence was made to offend the eyes of anyone who saw it."
"Horrifying design choices aside though, there is something about it that feels... off, somehow. Like a prickle along my back. Feels creepy. "
"Hm. Should I ignore every single instinct screaming DANGER and grab the thing, or should I leave it alone? "
(option: #grab_orb or #leave_orb)
(jump to #grab_orb)
scene: office - zoom out to full, -bg_orb)
(Insert Close Up Box)
(Show: Orb tape_full)
"I grab it, holding it close with one hand and searching for the end of the tape with the other. I rip."
#note- Expression: Drew ewf, bh, mg)
#note- Expression: Orb spike_top, tape_top)
"I am nearly stabbed by it, so I drop it faster than a demon's fetus because WHAT."
#note- Expression: Orb spike_middle, tape_middle)
"I stare unblinkingly. The Orb—because it deserves that capital \"O” for \"oh my god, you can't be serious”—lands on the wooden floorboards with a dull thunk. I'm pretty sure it made a new dent in the wood. "
#note- Expression: Orb spike_bottom, tape_bottom)
"And I'm pretty sure I'm trying to distract myself from thinking about the stabby, murderous bowling ball currently peeling itself from the tape."
#note- Expression: Drew ecf, bw, msh)
#note- Expression: Orb -spike_bottom, -tape_bottom)
"It rolls back to look(?) up at me. Erm, it's hard to tell. It doesn't have any eyes, so I'm assuming it has the eldritch-abomination equivalent to it. "
"Seconds pass by in silence. Neither of us move. "
"Should I . . . ?"
menu: 
    "poke_orb":
        jump poke_orb
    "don't_poke_orb":
        jump dont_poke_orb
label poke_orb:
#note- Expression: Drew ecf, bw, mf)
"I lean over and poke the Orb. "
"All of a sudden, I hear flesh being torn. Blood hits the floorboard. "
#note- Expression: Drew ewf, bf, msh, extra_dread)
"I glance down, numbly, at the blackened spikes driven through my torso and limbs. Red ran rivulets down the spikes and pooled eerily beneath the Orb. "
"I belatedly ask myself, Why did I think it was a good idea to touch it?"
scene: death_orb)
"The Orb retracts its spikes and I fall to the floor. "
"Dead."
(RETURN TO MAIN MENU)
(jump to #don't_poke_orb)
#note- Expression: Drew enf, bw, mf)
"Nope, not going to do it. Curiosity killed the cat and all that. I'm too sober to be making stupid decisions while the sun is still up. "
scene: hallway)
#note- Expression: Drew ens, msh)
"I briskly walked out of the room and—oh hell, it's following me. No thanks, bye."
scene: storage - left end + doll_chest
if not gone yet OR scene: 
    "…. black because garbled won't draw another room for one segment."
    "I slip into the closest door across the hall and slam the door shut. "
    #note- Expression: Drew ewf, bf, mg)
    "There's a thunk. Then another thunk. And then to my horror, I hear it scraping against the doorknob. The knob is two feet higher than it, and it has no extra appendages to jiggle the handle. So how in the world did it manage to reach the knob?"
    "With a final crack (I'm fairly certain it stabbed the door that time), silence reigned. I waited a moment."
    "Then another. "
    #note- Expression: Drew ec, bh, msh)
    "Three beats pass before I breathe a sigh of relief, steppin away from the door. It seems like it's gone."
    #note- Expression: Drew ecs, bw, mf)
    "... At least for now."
if not storage_explored::
    "I finally look at my settings."
else
    "I let my eyes adjust to the darkness and squint around the room I hid in. Bathroom, huh…"
    "I'll worry about it after I'm not hiding."
    if storage_1:
        jump living_room_2
    else:
        jump storage_1
label leave_orb
    #note- Expression: Drew ecf, bw, mf)
    "Nope, I'm not dealing with this. I have a healthy sense of self-preservation, and my self-preservation is telling me to walk away."
    "So that's precisely what I did. I turned around and walked the way I came in. "
    if storage_explored:
        #note- Expression: Drew ecs, bn, mg)
        "After what happened in the Storage room, there is no way I'm going to mess with anything wrapped in yellow tape. For all I know, it could be a murderous snow globe filled with murderous little snowmen. No thanks."
        #note- Expression: Drew ecf, bh, mf)
        "I open the door a sliver and peek out of the office. The hallway was blessedly empty, devoid of any mannequins or any other off-brand Halloween knock off."
        "I slip out of the room with my basket of junk, making sure to close the door shut behind me. Maybe I'll have better luck cleaning out the living room first. "
        jump living_room_2
    else:
        #note- Expression: Drew ewf, bh, msh)
        "At least until I heard a bang. "
        "It was the same sound from earlier, before I started cleaning the office. Just what is causing that racket?"
        scene: hallway
        "I swiftly stepped out into the hallway right as another bang happened. It sounded like it came from... the storage room? "
        jump storage_1
