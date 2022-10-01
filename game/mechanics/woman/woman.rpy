init:
    $ renpy.music.register_channel("ambient","sfx",True,tight=True)

init -1 python:
    import random

    def random_times(min, max, duration):
        # TODO: Maybe add a difficulty curve here.
        count = 0.0
        numbers = [0]
        while count <= (duration-woman_prompt_timeout):
            ran = random.uniform(min, max)
            numbers.append(numbers[-1]+ran)
            count += ran
        numbers.pop(0)
        numbers.pop()
        return numbers

    def random_prompt_pos():
        return (random.randint(300, config.screen_width-300), random.randint(300, config.screen_height-300))

    def ranu(tag, min, max, t, st, at):
        glog(tag)
        setattr(renpy.store, tag, random.uniform(min, max))

        return None

    def rani(tag, min, max, t, st, at):
        glog(tag)
        setattr(renpy.store, tag, random.randint(min, max))
        SetVariable(tag, random.randint(min, max))()
        glog(getattr(renpy.store, tag))
        return None

transform brow_shake:
    ease .08 offset (1, 0)
    ease .08 offset (0, 1)
    ease .06 offset (2, 0)
    ease .06 offset (0, 2)
    repeat

transform iris_shake:
    linear random.uniform(0.15, 0.35) xoffset -8
    pause random.uniform(0.5, 0.85)
    linear random.uniform(0.15, 0.35) xoffset 8
    pause random.uniform(0.5, 0.85)
    repeat

transform mouth_shake:
    ease .08 offset (2, 0)
    ease .08 offset (0, 1)
    ease .06 offset (1, 0)
    ease .06 offset (0, 2)
    repeat

transform woman_wiggle(tag="mouth_1"):
    alpha 0.0
    align (0.5, 0.5)
    parallel:
        block:
            choice:
                pause 0.5
            choice:
                pause 1.5
            choice:
                pause 3.5
        linear 0.85 alpha 1.0
        block:
            choice:
                pause 0.5
            choice:
                pause 1.5
            choice:
                pause 2.0
        linear 0.85 alpha 0.0
        block:
            choice:
                pause 0.5
            choice:
                pause 1.5
            choice:
                pause 3.5
        repeat
    parallel:
        block:
            choice:
                ease 0.65 rotate 3
            choice:
                ease 0.85 rotate 4
            choice:
                ease 0.95 rotate 5
        block:
            choice:
                ease 0.65 rotate -3
            choice:
                ease 0.85 rotate -4
            choice:
                ease 0.95 rotate -5
        repeat
    parallel:
        parallel:
            choice:
                ease 0.85 xoffset -35
            choice:
                ease 0.65 xoffset 35
            choice:
                ease 0.85 xoffset -25
            choice:
                ease 0.95 xoffset 25
        parallel:
            choice:
                ease 0.85 yoffset -35
            choice:
                ease 0.65 yoffset 35
            choice:
                ease 0.85 yoffset -25
            choice:
                ease 0.95 yoffset 25
        repeat

transform hair_1:
    pos (int(config.screen_width/2),  int(config.screen_height/2)-50)

transform hair_2:
    pos (int(config.screen_width/2),  int(config.screen_height/2)-50)

transform hair_3:
    pos (int(config.screen_width/2),  int(config.screen_height/2)+50)

transform hair_4:
    pos (int(config.screen_width/2)-50,  int(config.screen_height/2)+50)

transform hair_5:
    pos (int(config.screen_width/2),  int(config.screen_height/2)-50)

screen drew_woman_bg:
    add "mechanics/woman/background.png"
    fixed:
        fit_first True
        align (0.5, 1.0)
        add "mechanics/woman/drew_base.png"
        add "mechanics/woman/drew_brows.png" xalign 0.5 ypos 120 at brow_shake
        add "mechanics/woman/drew_eyes_open.png" xalign 0.5 ypos 150
        add "mechanics/woman/drew_irises.png" xalign 0.5 ypos 155 at iris_shake
        add "mechanics/woman/drew_mouth.png" xalign 0.5 ypos 225 at mouth_shake

    add "mechanics/woman/woman/mouth_3.png" at woman_wiggle
    add "mechanics/woman/woman/eyes_1.png" at woman_wiggle
    add "mechanics/woman/woman/eyes_2.png" at woman_wiggle
    add "mechanics/woman/woman/eyes_3.png" at woman_wiggle
    add "mechanics/woman/woman/hair_1.png" at woman_wiggle, hair_1
    add "mechanics/woman/woman/hair_2.png" at woman_wiggle, hair_2
    add "mechanics/woman/woman/hair_3.png" at woman_wiggle, hair_3
    add "mechanics/woman/woman/hair_4.png" at woman_wiggle, hair_4
    add "mechanics/woman/woman/hair_5.png" at woman_wiggle, hair_5
    add "mechanics/woman/woman/mouth_1.png" at woman_wiggle
    add "mechanics/woman/woman/mouth_2.png" at woman_wiggle

screen woman_game:
    timer woman_length action Jump("woman_success")
    key list(woman_keys) action Jump("woman_noise")
    for t in random_times(woman_frequency_min, woman_frquency_max, woman_length):
        timer t action Show("qte_prompt")

screen qte_prompt():
    default k = random.choice(woman_keys)
    key k action Hide("qte_prompt") # TODO: Add positive feedback.
    key [key for key in woman_keys if key is not k] action Jump("woman_noise") # TODO: Add positive feedback.
    timer woman_prompt_timeout action Jump("woman_noise")
    frame:
        xysize (100, 100)
        pos random_prompt_pos()
        text "[k]" align(0.5, 0.5)

label woman_noise:
    hide screen qte_prompt
    "woman" "I heard that!"
    if woman_chances > 0:
        $ woman_chances -= 1
        "woman" "{i}*giggle*{/i}"
        "woman" "Let's try this one more time. Don't make a peep!"
        call screen woman_game
    else:
        jump woman_bad_end
    return

label woman_bad_end:
    hide screen qte_prompt
    jump failed_woman_game

label woman_success:
    hide screen qte_prompt
    jump beat_woman_game

label start_woman_game:
    play ambient "mechanics/woman/SFX_Spooktober_Doll_Whispering.ogg"
    show screen drew_woman_bg with dissolve
    call screen woman_game
    return
