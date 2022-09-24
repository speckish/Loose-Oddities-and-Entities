# Customizable variables
define swing_speed = 3.0 # Seconds it takes for a swing to traverse the bar once.

default doll_attempts = 0
default swing_force = 0.0

image swing_bar = "mechanics/doll/swing_bar.png"
image swing_indicator = "mechanics/doll/swing_indicator.png"
image transparent = "#ff000001"

screen doll_game():
    fixed:
        fit_first True
        align (0.975, 0.5)
        add "swing_bar"
        add swing_indicator
    imagebutton:
        idle "transparent"
        action Return()

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

label start_doll_game:
    $ swing_indicator = Transform(child="swing_indicator", function=swing_indicator_transform, align=(0.5, 0.5))
    jump doll_game_loop

label doll_game_loop:
    call screen doll_game
    if swing_force < -285:
        jump beat_doll_game
    else:
        $ doll_attempts += 1
        call expression ("miss_doll_"+str(doll_attempts))
        jump doll_game_loop

label miss_doll_1:
    "<First Miss>"
    return

label miss_doll_2:
    "<Second Miss>"
    return

label miss_doll_3:
    "<Third Miss>"
    "<Bad End>"
    jump end_game

label beat_doll_game:
    "*CRACK*"
    "Shards of the doll's head fly in all directions and you're left with the jagged edge of it's porcelain neck staring back at you."
    "<Sucess>"
    jump end_game
