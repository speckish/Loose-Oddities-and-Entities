default doll_attempts = 0
default swing_force = 0.0

image swing_bar = "mechanics/doll/swing_bar.png"
image swing_indicator = "mechanics/doll/swing_indicator.png"
image doll = "mechanics/doll/doll.png"
image hammer = "mechanics/doll/hammer.png"
image missed_hit = "mechanics/doll/missed_hit.png"
image doll_background = "mechanics/doll/background.png"
image transparent = "#ff000001"

transform doll_miss:
    pause 0.85
    linear 0.05 rotate 2
    linear 0.15 rotate -4
    linear 0.15 rotate 0

transform missed_hit_flash:
    alpha 0.0
    pause 0.65
    block:
        linear 0.5 alpha 1.0 offset (25, -25)
        linear 0.5 alpha 0.65 offset (0, 0)
        repeat

transform doll_hit:
    pause 0.85
    parallel:
        linear 0.05 rotate 2
        linear 0.15 rotate -4
        linear 0.10 rotate 6
        linear 0.05 rotate -2
    parallel:
        linear 0.25 zoom 1.0025
        linear 0.5 zoom 1.0

transform hammer_miss(sf):
    rotate -sf/420*30
    anchor (0.5, 0.5)
    pos (0.75, 0.85)
    pause 0.5
    easeout_back 0.5 rotate -30 xpos 0.25
    pause 0.25
    linear 1.0 pos (0.75, 0.85) rotate -sf/420*30

transform hammer_hit(sf):
    rotate -sf/420*30
    anchor (0.5, 0.5)
    pos (0.75, 0.85)
    pause 0.5
    ease_back 0.5 rotate -30 xpos 0.5
    pause 0.5
    linear 1.0 pos (0.75, 0.85) rotate -sf/420*30

screen doll_game(interactable=True):
    key ["K_SPACE", "K_KP_ENTER", "K_RETURN"] action Return()
    add "doll_background"
    add "doll" anchor (0.5, 0.5) pos (0.25, 1.0)
    add Transform("hammer", function=hammer_transform) anchor (0.5, 0.5) pos (0.75, 0.85)
    if interactable:
        fixed:
            fit_first True
            align (0.975, 0.5)
            add "swing_bar"
            add swing_indicator
        imagebutton:
            idle "transparent"
            action Return()

screen doll_game_attempt(success=False):
    add "doll_background"
    if success:
        add "doll" anchor (0.5, 0.5) pos (0.25, 1.0) at doll_hit
        add "hammer" at hammer_hit(swing_force)
    else:
        add "missed_hit" at missed_hit_flash pos (0.30, 0.10)
        add "doll" anchor (0.5, 0.5) pos (0.25, 1.0) at doll_miss
        add "hammer" at hammer_miss(swing_force)


init -1 python:
    def swing_indicator_transform(t, st, at):
        if st <= swing_speed/2:
            t.yoffset = renpy.atl.warpers['linear']((st/(swing_speed/2))%1)*-420
        elif (st-swing_speed/2)%(swing_speed*2) <= swing_speed:
            t.yoffset = -420+renpy.atl.warpers['linear'](((st-swing_speed/2)%swing_speed)/swing_speed)*840
        else:
            t.yoffset = 420+renpy.atl.warpers['linear'](((st-swing_speed/2)%swing_speed)/swing_speed)*-840
        setattr(renpy.store, "swing_force", t.yoffset)
        return 0.0

    def hammer_transform(t, st, at):
        t.rotate = -swing_force/420*30
        return 0.0

label start_doll_game:
    $ swing_indicator = Transform(child="swing_indicator", function=swing_indicator_transform, align=(0.5, 0.5))
    show screen doll_game(False)
    call doll_intro
    jump doll_game_loop

label doll_game_loop:
    call screen doll_game with dissolve
    if swing_force < -285:
        show screen doll_game(False)
        pause 0.0
        hide screen doll_game
        show screen doll_game_attempt(True)
        with dissolve
        jump beat_doll_game
    else:
        $ doll_attempts += 1
        show screen doll_game(False)
        pause 0.0
        hide screen doll_game
        show screen doll_game_attempt
        with dissolve
        call expression ("miss_doll_"+str(doll_attempts))
        jump doll_game_loop
