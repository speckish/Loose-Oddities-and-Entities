default horned_frustration = 0
default horned_game = False

init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        if horned_game:
            renpy.random.shuffle(items)
        return renpy_menu(items)

image hanging_horned_eyes_confused:
    "mechanics/horned/horned_confused_eyes.png"
    random.uniform(1.0, 2.5)
    "mechanics/horned/horned_closed_eyes.png"
    random.uniform(0.25, 0.5)
    repeat

image hanging_horned_eyes_mad:
    "mechanics/horned/horned_mad_eyes.png"
    random.uniform(5.0, 8.5)
    "mechanics/horned/horned_closed_eyes.png"
    random.uniform(1.0, 1.5)
    repeat

image hanging_horned_eyes_happy:
    "mechanics/horned/horned_happy_eyes.png"
    random.uniform(2.5, 5.0)
    "mechanics/horned/horned_closed_eyes.png"
    random.uniform(0.5, 0.85)
    repeat

image hanging_horned_mouth_happy = "mechanics/horned/hanging_horned_mouth_happy.png"
image hanging_horned_mouth_confused = "mechanics/horned/hanging_horned_mouth_confused.png"
image hanging_horned_mouth_mad = "mechanics/horned/hanging_horned_mouth_mad.png"
image horned_background = "mechanics/horned/background.png"

layeredimage hanging_horned:
    always "mechanics/horned/horned_base.png"
    group eyes auto:
        attribute happy default
        attribute confused
        attribute mad

    group mouth auto:
        attribute happy default
        attribute confused
        attribute mad

label start_horned_game:
    show horned_background
    show hanging_horned:
        anchor (0.5, 0.535)
        pos (0.25, 0.0)
        rotate 5
        block:
            ease_cubic 5 rotate -5
            ease_cubic 5 rotate 5
            repeat
    with fade
    call horned_intro
    $ horned_game = True
    # In case we want to run this multiple times.
    $ questions = [q for q in horned_questions]
    $ random.shuffle(questions)
    while questions:
        call horned_question(*questions.pop(0))
        if horned_frustration >= horned_threshold:
            $ horned_game = False
            jump horned_fail
    $ horned_game = False
    jump horned_success

screen horned_choice(items):
    style_prefix "choice"
    vbox:
        anchor (0.5, 0.5)
        pos 0.75, 0.75
        for i in items:
            textbutton i.caption action i.action

screen horned_say(who, what):
    text what id "what" pos (0.5, 0.25)
