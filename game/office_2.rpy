label office_2:
    $ if not orb_unwrapped:
        scene hallway 
        "Alright. Time to deal with whatever creature that dwells in Grandpa's office."
        scene office
        "I open the door to the horror once more. Dust and silence greeted me. Now that I knew what was going on in this house, I won't find myself caught off guard a second time. Not like with the mannequin. I'm ready for whatever the thing in the office throws my way. "
        "That said..."
        scene office
        #note zoom into orb
        "I cautiously approach the shelf."
        "The round bowling ball-esque item wrapped in the yellow eyesore sat there innocently, right where I left it."
        "I know for certain that this is an entity Grandpa locked up in the office. There is no other thing it could be."
        scene office
        #note close up of Orb into orb
        "I pick it up and turn it over in my hands. I narrow my gaze, contemplating."
        "Now... What should I do with you?"
        menu:
            "Should I..."
            "grab the orb":
                jump grab_orb
            "trash the orb":
                jump trash_orb

        label poke_orb:
            "I poke the Orb."
            "All of a sudden, I hear flesh being torn. Blood hits the floorboard."
            "I glance down, numbly, at the blackened spikes driven through my torso and limbs. Red ran rivulets down the spikes and pooled eerily beneath the Orb."
            "I belatedly ask myself, Why did I think it was a good idea to touch the stab-happy bowling ball?"
            "The Orb retracts its spikes and I fall to the floor. "
            "Dead."
            return

        label dont_poke_orb2:
            "Nope, not going to do it. Curiosity killed the cat and all that. I'm too sober to be making stupid decisions while the sun is still up." 
            "I briskly walked out of the room and—oh hell, the bowling ball murder child is following me. No thanks, bye."
            "I zip to the stairs until I hear a thunk."
            "I turn."

        label trash_orb:
            "Hm... The fireplace is downstairs, but I doubt it will melt whatever this is. Maybe there's something else I could... ?"
            "I glance around the office and my gaze lands on the window. I stride over and throw open the curtains (which was a mistake as I hack my lungs out, because wow, these drapes are dusty), only to confirm it was as taped closed as the rooms downstairs."
            "I pluck at the ends until I can get a grip and rip the tape away. After that, it's quick work popping the latch and sticking my head outside." 
            "The first thing I noted was that the second floor was a relatively good distance from the ground."
            "The second thing I took note of was that the mysterious sphere in my hands was relatively heavy."
            "The third thing was something I remembered was from high school physics class."
            "What was it again? Something about Newton and how an apple knocked a few screws loose when he was younger?"
            "Oh well. This is heavier than an apple anyway. Bombs away!"
            "I awkwardly toss the bowling ball and watch it sail beautifully out the window. Like a ten-pound dove a colorblind toddler dumped paint on. It was a truly lovely way to say goodbye to that eyesore."
            "... But then it plunked to the ground still intact, and all my hopes and dreams were dashed just like that."
            "I stare at it mournfully. Why did Grandpa have to neglect his lawn to the point that it had soft grass made for cushioning the fall of a potentially cursed, murderous snowglobe with murderous little snowmen? "
            "Ugh. Well, at least it's not moving. I'll throw it out with the rest of the trash later"
            jump rooms_choice

    $ if orb_unwrapped:
        scene hallway
        #note close up of orb
        "I watch as the Orb rolls into a door, then another across the hall, and then back to a third door with a loud thunk. Maybe I was hasty earlier calling it a bowling ball."
        "Sure, it has the size and weight of a bowling ball. But I was clearly watching the world's slowest, oversized ping pong ball in motion."
        "It honestly looks... pretty pathetic."
        "No, wait. Not “pretty pathetic.” "
        "“Absolutely, completely, and incomparably pathetic” is a more apt descriptor. It's like watching a blind puppy stumble around smacking into doors, trying to find its clearly absent owner. It was nearly enough to tug at my dead heartstrings."
        "But then again, blind puppies don't try to stab you. Soooooo..."
        "All of a sudden, it stops rolling. It stands still in the middle of the hallway."
        "Something prickles the back of my subconscious. I had a sneaking suspicion that it was my senses telling me that the Orb was watching me like the eldritch abomination that it is. "
        "It jerks back. Then it wiggles. "
        "And yes, seeing it happen was as weird as describing it. "
        "Fortunately, I did not have to dwell on how off-kilter that was, as the Orb rolled towards me like a good, murderous, puppy dog bowling ball. "
        menu:
            "Thinking quick, I—"
            "stop":
                jump stop_orb
            "Retreat":
                jump lead_orb_downstairs

        label stop_orb:
            d "Stop."
            "It freezes."
            "I raise a brow."
            "Huh, what do you know? It really is like a puppy. I wonder if it would roll over if I ask—"
            "I clear my throat."
            "The Orb tilts to the side like a puppy would with its head, and the urge to ask it to roll over crashes back at full strength. "
            "Once again, I relentlessly beat down the impulse to the depths of my psyche from whence it hailed."
            d "I'm assuming you understand everything I'm saying since you stopped. Right?"
            "It wiggles. "
            d ".. Uh, I have no idea what that means. Can you just—roll a circle for yes, and side to side for no?"
            "It completes a small circuit on the floor. "
            d "Okay, that's good to know."
            if drew_killed:
                "I know I should be trying to get rid of this thing. I mean, I've already committed to disposing the others."
                "But, I feel like trying to hurt the little guy would be like trying to hurt a puppy. A blind puppy. And with a neglectful owner on top of that."
                "I sigh. "
                "Murderous tendencies aside, the Orb can be kinda cute when it wants to be. I might as well let it go."
                "I mean, there's no harm in letting it go. Right?"
                D "How about you and I strike a deal? You want to leave this house. I want you gone. So why don't you roll down the steps and out the front door so we can both have what we want, alright?”"
                "The Orb rolls back and forth. "
                D "Oh. That's a problem. Why not?"
                "It jerks ramrod straight (or about as straight as can be for something so .. rotund) and vibrates—I want to say “excitedably,” but but for all I know, it was quivering in murderous rage."
                scene hallway
                #note hide Close up + zoom into door at the end of the hall
                "Thankfully for me, it seemed to be the former. It zips over to one of the doors and repeatedly smacks head first (orb-first?) against it, leaving more scratches on the already scratched wood. "
                "I raise a brow and stride over, opening the door. Inside was a small closet filled to the brim with more odd knicknacks (none of them sentient from what I can tell—which is great) piled precariously on top of each other. I glanced down at the Orb quivering in excitement at the mess. "
                D "Oh. So, you want something from here."
                "It circles. "
                "I nodded resolutely to myself and took a deep breath."
                D "Alright. If I find it for you, will you leave?"
                "Another circle. "
                D "Great. Time to go digging."
                #note MINIGAME
                #note if minigame lost
                if minigame_win:
                    jump minigameWin
                else:
                    jump minigameLoss
label minigameWin:
    scene hallway
    #note zoom out + close up of Orb
    "It zips happily around the hallway, cowboy hat firmly impaled on its head. It zooms around me and I chuckle. "
    d "I'll take it this means you're happy with the hat then."
    "It rapidly circles over and over in a black blur. I smile wryly, a little fondly at its antics. "
    "Oh yeah. This thing is real happy."
    scene hallway
    #note hide close up of orb
    "It flings itself over the staircase's banister and crashlands downstairs. "
    "I blink. I blink again. "
    "...This thing won't tear the house down, will it?"
    jump rooms_choice
label minigameLoss:
    "I see the orb shaking at my feet, back and forth, back and forth. I stop my search."
    d "I'm not sure what you're looking for then, sorry."
    "It rapidly spins in one place and before I can even close my mouth, I feel something sharp rip through my gut. I try to step away from the pain, but I just hit the closet door."
    "The spike the orb stabbed me with tears out of my torso at the same speed it entered and I slid down to the floor, feeling cold."
    "The orb bumps into my thigh several times, but all I can do is stare until everything goes black."
    #note is this the end of the game?
    return

label lead_orb_downstairs:
    "I step back."
    "It rolls closer. "
    "I take another step back."
    "I builds momentum. "
    scene hallway
    #note hide close up of orb
    scene front_door
    scene living_room
    #note multiple scenes?
    "I swivel around and book it, zipping down the stairs. I can hear it thunking noisily (and rapidly) down the steps behind me. I practically fly down the banister and throw myself to the living room, dashing—"
    menu:
    "Straight":
        jump run_straight
    "To the side":
        jump run_gay

label run_straight:
    "—straight forward, charging like a bull."
    "And then something hits me in the back. "
    "Stabs me in the back. "
    "I glance down at the billion black spikes skewering my torso. Blood bubbles in the back of my throat. I cough, red dripping down my chin and splattering on the floorboards."
    "Godda—"
    "I fell forward and fell silent."
    scene orb_death
    return

label run_gay:
    "—to the side, flinging myself out of the way as the Orb hurtles like a demented canonball right through where my head was once upon a time. "
    "It slammed into the sofa with a crack. It teeters, dazed, but not for long. "
    if with_cards:
        "The deck of cards wriggles in my pocket. I glance down. "
        "It shoots a card like a bullet and lands gracefully, inches shy of a roll of horrendously yellow tape—"
        "Wait. I know that eyesore of a shade anywhere. "
        "I lunge to the mantle and snatch it off, right as the Orb turns its full attention on me. It barrels off the couch and jumps. "
        scene living_room
        #note Close Up of Orb
        "Thinking quick, I rip off the tape and slap it on the murderous canonball as it sailed by. It slammed into the wall with the tape trailing after it. It jolted. Panicked. It zoomed this way and that, trying to shake the tape off it to no avail. "
        "Instead, all it did was entangle itself further."
        "Soon enough, it stopped moving altogether. Only a few slivers of black peeked out between the wrappings. "
        "I cautiously approach and pick it up. "
        "Ah, wait. It is still moving. It's very faint, but I could pick up its trembling. I can almost imagine it whimpering, pleading with me not to fully bind it back to its lonely imprisonment once more. "
        "I felt sad for the little guy. "
        "But not sad enough considering it tried to stab me. I quickly wrap the tape around all the blind spots until it resembled the yellow eyesore from earlier once more. "
        "I'll take it out with the rest of the trash later. "
    if not with_cards:
        "Thinking fast, I lunge for the nearest weapon. "
        "I brandish a broken metal hockey stick (why does grandpa even have this?) like it was a sword capable of protecting me and not a very desperate attempt at a makeshift weapon."
        "Only one way to find out. "
        scene living_room
        #note - Close Up of Orb)
        "The Orb stops teetering and turns its full attention on me. It barrels off the couch and rockets a spike at me, but I manage to parry it in the knick of time. It stabs me again. And again. I meet it blow for blow, spike to stick, black on silver, each attack parried with a swipe and a parry. "
        "It stabs at my feet and I leap onto the couch. I dive as it shoots a spike, impaling the cushions, but another swift strike grazes my calf before I could recover. "
        "I hiss. I grab a throw pillow and did what it was named for—throw it. "
        "It slams into the Orb. It didn't do much in the way of hurting it, but the sudden darkness was enough to startle it into skewering it over and over in panic."
        "I take the chance. I swing the hockey stick like the hockey player I never was and smack it. "
        scene living_room
        #note - hide Close Up of Orb)
        "It sails, pillow and all, slamming into the iron fire grate with a sickening crack."
        scene living_room
        #note - zoom into fire grate)
        "It slides down with a dull thunk. I cautiously poke it. Once. Twice."
        "I knock the pillow off the Orb and—oh. "
        "A thick crack splits through it. Long and jagged, spewing hazy wisps of black smoke into the air. "
        "I poke it again and—okay, yeah. I'm fairly certain it's dead. Or whatever constitutes as “dead” for stab-happy eldritch abominations in the form of bowling balls. "
        if rooms_left > 0:
            "Well, at least the office is clear. One down and—how many rooms are there left?"
            if office_last:
                "Thankfully, the office was the last one on my list of rooms to clear out."
        jump rooms_choice







