define horned_questions = [("I want to eat...", "cookie", "dirt", "human"),
                           ("I want to smell...", "flowers", "coffee", "sulfur"),
                           ("I want to see...", "sun", "ground", "darkness")]
default horned_threshold = 2

default horned_frustration = 0

default horned_game = False

init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        if horned_game:
            renpy.random.shuffle(items)
        return renpy_menu(items)

label start_horned_game:
    "You start cutting down the horned and they start chatting you up."
    $ horned_game = True
    # In case we want to run this multiple times.
    $ questions = [q for q in horned_questions]
    $ random.shuffle(questions)
    while questions:
        call horned_question(*questions.pop(0))
        if horned_frustration >= horned_threshold:
            jump horned_fail
    jump horned_success

screen horned_choice(items):
    style_prefix "choice"
    vbox:
        anchor (0.5, 0.5)
        pos 0.75, 0.75
        for i in items:
            textbutton i.caption action i.action

screen horned_say(who, what):
    text what id "what" align (0.35, 0.25)

label horned_question(question, best, mid, worst):
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
    # Show horned happy.
    $ ans = answer.capitalize()
    "Horned" "Yes! That's it! [ans]!"
    "Horned" "[question][answer]..."
    return

label worst_answer(answer, question):
    # Show horned mad.
    $ horned_frustration += 1
    "Horned" "NO. I don't think that's right."
    return

label okay_answer(answer, question):
    # Show horned confused.
    $ horned_frustration += 1
    $ ans = answer.capitalize()
    "Horned" "[ans]? That doesn't quite sound right."
    "Horned" "[question][answer]? I don't think that's what I meant."
    return

label horned_fail:
    "<Failed the Horned's game.>"
    jump end_game

label horned_success:
    "<Succeeded at the Horned's game.>"
    jump end_game
