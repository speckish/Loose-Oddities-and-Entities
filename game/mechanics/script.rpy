#########
# Cards #
#########

# The card the cards 'want' you to pick (can be "good", "bad", or "neutral").
default cards_desired_card = "good"

# Intro prompt.
label cards_intro:
    "Now, pick, and pick correctly or else!"
    return

# Ending labels based on your choice.
label cards_picked_good_card:
    "Lucky guess. You pass for now."
    jump end_game

label cards_picked_bad_card:
    "OOHHH, so close...but not close enough. Guess you die now!"
    jump end_game

label cards_picked_neutral_card:
    "*SHRUG*"
    jump end_game

##########
# Horned #
##########

# Questions the horned will ask, followed by the possible answers is the order
# of best, neutral, and worst. Can contain a variable number of prompts.
define horned_questions = [("I want to eat...", "cookie", "dirt", "human"),
                           ("I want to smell...", "flowers", "coffee", "sulfur"),
                           ("I want to see...", "sun", "ground", "darkness")]

# Number of wrong guesses until you fail.
default horned_threshold = 2

# Intro prompt.
label horned_intro:
    "You start cutting down the horned and they start chatting you up."
    return

# Question prompts and answer labels.
label horned_question(question, best, mid, worst):
    if horned_frustration:
        show hanging_horned confused
    else:
        show hanging_horned happy
    "Horned" "[question] umm, what do you call it again?"
    menu:
        "[question] umm, what do you call it again?"
        "[best]":
            call best_answer(best, question)
        "[worst]":
            call worst_answer(worst, question)
        "[mid]":
            call okay_answer(mid, question)
    return

label best_answer(answer, question):
    show hanging_horned happy
    $ ans = answer.capitalize()
    "Horned" "Yes! That's it! [ans]!"
    "Horned" "[question][answer]..."
    return

label worst_answer(answer, question):
    show hanging_horned mad
    $ horned_frustration += 1
    "Horned" "NO. I don't think that's right."
    return

label okay_answer(answer, question):
    show hanging_horned confused
    $ horned_frustration += 1
    $ ans = answer.capitalize()
    "Horned" "[ans]? That doesn't quite sound right."
    "Horned" "[question][answer]? I don't think that's what I meant."
    return

# Ending labels based on your choice.
label horned_fail:
    show hanging_horned mad
    "<Failed the Horned's game.>"
    jump end_game

label horned_success:
    show hanging_horned happy
    "<Succeeded at the Horned's game.>"
    jump end_game

#############
# Mannequin #
#############

# Intro prompt.
label mannequin_intro:
    "The mannequin game!"
    "Take off the bandages and stitches but don't touch the worms!"
    return

# Ending labels based on your choice.
label mannequin_success:
    show screen mannequin_game(False)
    "You did it! <Won mannequin game.>"
    jump end_game

label mannequin_fail:
    show screen mannequin_game(False)
    "You failed! <Lost mannequin game.>"
    jump end_game

#######
# Orb #
#######

# The item that the orb wants you to choose (the goal item).
define orb_item = "snowglobe"

# Number of attempts the orb will give you before you fail.
define orb_attempts = 3

# Intro prompt.
label orb_intro:
    "Try to figure out what the orb wants."
    return

# Prompt when you guess wrong but can try again.
label orb_incorrect(i):
    $ i_cap = i.capitalize()
    "[i_cap] was not what the orb wanted. Try again."
    return

# Ending labels based on your choice.
label orb_success:
    "<You succeeded at the orb's task.>"
    jump end_game

label orb_fail(i):
    $ i_cap = i.capitalize()
    "[i_cap] was not what the orb wanted."
    "<You failed the orb's task.>"
    jump end_game

########
# Doll #
########

# Seconds it takes for a swing to traverse the bar once.
define swing_speed = 2.5

# Intro labels.
label doll_intro:
    "Take a swing, and don't miss!"
    return

# Swing attempt labels.
label miss_doll_1:
    "<First Miss>"
    return

label miss_doll_2:
    "<Second Miss>"
    return

# For how many chances you get, the number of attempt labels must be the same.
# The last attempt label is always treated as the fail label.
label miss_doll_3:
    "<Third Miss>"
    "<Bad End>"
    jump end_game

# Success label.
label beat_doll_game:
    "*CRACK*"
    "Shards of the doll's head fly in all directions and you're left with the jagged edge of it's porcelain neck staring back at you."
    "<Sucess>"
    jump end_game

#########
# Woman #
#########
