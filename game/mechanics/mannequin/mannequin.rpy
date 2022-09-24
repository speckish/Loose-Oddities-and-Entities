###
define back_pos = (892, 540)
define open_scar_pos = (879, 705)
define open_scar_mask_pos = (878, 704)

define left_bandage_3_pos = (756, 715)
define left_bandage_2_pos = (747, 791)
define left_bandage_1_pos = (750, 971)
define right_bandage_3_pos = (1028, 711)
define right_bandage_2_pos = (1035, 796)
define right_bandage_1_pos = (1056, 974)

define worm_pos = (1268, 398)

define left_cinch_1_pos = (1039, 484)
define left_stitch_1_pos = (1044, 486)
define left_cinch_2_pos = (1029, 585)
define left_stitch_2_pos = (1033, 587)
define left_cinch_3_pos = (1015, 690)
define left_stitch_3_pos = (1018, 692)
define left_cinch_4_pos = (998, 790)
define left_stitch_4_pos = (995, 791)
define left_cinch_5_pos = (986, 933)
define left_stitch_5_pos = (992, 934)
define right_cinch_1_pos = (724, 496)
define right_stitch_1_pos = (736, 492)
define right_cinch_2_pos = (739, 596)
define right_stitch_2_pos = (747, 598)
define right_cinch_3_pos = (754, 702)
define right_stitch_3_pos = (754, 703)
define right_cinch_4_pos = (767, 797)
define right_stitch_4_pos = (763, 797)
define right_cinch_5_pos = (786, 955)
define right_stitch_5_pos = (786, 951)
###

image mannequin_background = "mechanics/mannequin/background.png"
image mannequin_back = "mechanics/mannequin/back.png"
image open_scar = "mechanics/mannequin/open_scar.png"
image open_scar_mask = "mechanics/mannequin/open_scar_mask.png"
image left_bandage_3 = "mechanics/mannequin/left_bandage_1.png"
image left_bandage_2 = "mechanics/mannequin/left_bandage_2.png"
image left_bandage_1 = "mechanics/mannequin/left_bandage_3.png"
image right_bandage_3 = "mechanics/mannequin/right_bandage_1.png"
image right_bandage_2 = "mechanics/mannequin/right_bandage_2.png"
image right_bandage_1 = "mechanics/mannequin/right_bandage_3.png"
image left_cinch_1 = "mechanics/mannequin/left_cinch_1.png"
image left_stitch_1 = "mechanics/mannequin/left_stitch_1.png"
image worm = "mechanics/mannequin/worm.png"
image left_cinch_2 = "mechanics/mannequin/left_cinch_2.png"
image left_stitch_2 = "mechanics/mannequin/left_stitch_2.png"
image left_cinch_3 = "mechanics/mannequin/left_cinch_3.png"
image left_stitch_3 = "mechanics/mannequin/left_stitch_3.png"
image left_cinch_4 = "mechanics/mannequin/left_cinch_4.png"
image left_stitch_4 = "mechanics/mannequin/left_stitch_4.png"
image left_cinch_5 = "mechanics/mannequin/left_cinch_5.png"
image left_stitch_5 = "mechanics/mannequin/left_stitch_5.png"
image right_cinch_1 = "mechanics/mannequin/right_cinch_1.png"
image right_stitch_1 = "mechanics/mannequin/right_stitch_1.png"
image right_cinch_2 = "mechanics/mannequin/right_cinch_2.png"
image right_stitch_2 = "mechanics/mannequin/right_stitch_2.png"
image right_cinch_3 = "mechanics/mannequin/right_cinch_3.png"
image right_stitch_3 = "mechanics/mannequin/right_stitch_3.png"
image right_stitch_4 = "mechanics/mannequin/right_stitch_4.png"
image right_cinch_4 = "mechanics/mannequin/right_cinch_4.png"
image right_stitch_4 = "mechanics/mannequin/right_stitch_4.png"
image right_cinch_5 = "mechanics/mannequin/right_cinch_5.png"
image right_stitch_5 = "mechanics/mannequin/right_stitch_5.png"

default stitches_left = set([1, 2, 3, 4, 5])
default stitches_right = set([1, 2, 3, 4, 5])

default bandage_left = 3
default bandage_right = 3

transform worm_wiggle(s):
    xoffset 115*s
    zoom 0.0
    block:
        choice:
            yzoom 1.0
        choice:
            yzoom -1.0
    choice:
        pause 0.5
    choice:
        pause 0.25
    choice:
        pause 0.75
    parallel:
        linear 1.5 xoffset 0
    parallel:
        linear 2.5 zoom 1.0
    parallel:
        linear 0.125 rotate 5
        block:
            linear 0.25 rotate -10
            linear 0.25 rotate 10
            repeat


transform stitch_pop(s):
    linear 0.25 zoom 1.25
    parallel:
        linear 0.5 zoom 1.0
    parallel:
        linear 1.0 xoffset 120*s
    parallel:
        linear 1.25 yoffset 800
    parallel:
        choice:
            linear 1.5 rotate 360
            rotate 0
            repeat
        choice:
            rotate 360
            linear 1.5 rotate 0
            rotate 360
            repeat

transform bandage_drop(s):
    linear 0.5 xoffset 200*s yoffset 300 rotate 50*s

screen mannequin_game:
    if not stitches_left and not stitches_right:
        timer 1.5 action Jump("mannequin_success")
    add "mannequin_background"
    add "mannequin_back" anchor (0.5, 0.5) pos back_pos
    add "open_scar" anchor (0.5, 0.5) pos open_scar_pos
    for i in range(1,6):
        use worm("left", i)
        use worm("right", i)
    add "open_scar_mask" anchor (0.5, 0.5) pos open_scar_mask_pos
    for i in range(1,6):
        use stitch("left", i)
        use stitch("right", i)
    use bandage("left")
    use bandage("right")
    for i in range(1,6):
        use top_stitch("left", i)
        use top_stitch("right", i)

screen worm(side, i):
    if not i in getattr(renpy.store, "stitches_%s" % side):
        imagebutton:
            at worm_wiggle(1 if side == "right" else -1)
            focus_mask True
            idle "worm"
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_cinch_%i_pos" % (side, i))
            action Jump("mannequin_fail")

# Could use some feedback like a hover or a cursor change
screen stitch(side, i):
    if i in getattr(renpy.store, "stitches_%s" % side):
        add "%s_cinch_%i" % (side, i):
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_cinch_%i_pos" % (side, i))
        imagebutton:
            # focus_mask True
            action RemoveFromSet(getattr(renpy.store, "stitches_%s" % side), i)
            idle "%s_stitch_%i" % (side, i)
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_stitch_%i_pos" % (side, i))

screen top_stitch(side, i):
    if not i in getattr(renpy.store, "stitches_%s" % side):
        add "%s_stitch_%i" % (side, i) at stitch_pop(-1 if side == "right" else 1):
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_stitch_%i_pos" % (side, i))

screen bandage(side):
    if getattr(renpy.store, "bandage_%s" % side):
        imagebutton:
            focus_mask True
            action SetVariable("bandage_%s" % side, getattr(renpy.store, "bandage_%s" % side)-1)
            idle "%s_bandage_%i" % (side, getattr(renpy.store, "bandage_%s" % side))
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_bandage_%i_pos" % (side, getattr(renpy.store, "bandage_%s" % side)))
    else:
        add "%s_bandage_1" % side:
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_bandage_1_pos" % side)
            at bandage_drop(1 if side == "right" else -1)

label start_mannequin_game:
    call screen mannequin_game
    return

label mannequin_success:
    "You did it! <Won mannequin game."
    jump end_game

label mannequin_fail:
    "You failed! <Lost mannequin game.>"
    jump end_game
