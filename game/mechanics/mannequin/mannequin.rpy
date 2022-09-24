###
define back_pos = (920, 535)
define open_scar_pos = (905, 707)
define open_scar_mask_pos = (905, 691)
define left_cinch_1_pos = (693, 393)
define left_cinch_2_pos = (707, 531)
define left_cinch_3_pos = (724, 693)
define left_cinch_4_pos = (733, 838)
define left_cinch_5_pos = (748, 1031)
define right_cinch_1_pos = (1119, 393)
define right_cinch_2_pos = (1105, 531)
define right_cinch_3_pos = (1088, 693)
define right_cinch_4_pos = (1078, 838)
define right_cinch_5_pos = (1064, 1031)
define left_stitch_1_pos = (691, 379)
define left_stitch_2_pos = (704, 518)
define left_stitch_3_pos = (720, 681)
define left_stitch_4_pos = (732, 833)
define left_stitch_5_pos = (746, 1026)
define right_stitch_1_pos = (1122, 379)
define right_stitch_2_pos = (1108, 518)
define right_stitch_3_pos = (1092, 681)
define right_stitch_4_pos = (1081, 833)
define right_stitch_5_pos = (1066, 1026)
define right_bandage_3_pos = (938, 678)
define left_bandage_3_pos = (721, 673)
define right_bandage_2_pos = (911, 794)
define left_bandage_2_pos = (710, 790)
define right_bandage_1_pos = (871, 1092)
define left_bandage_1_pos = (702, 975)
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
image worm_1 = "mechanics/mannequin/worm_1.png"
image worm_2 = "mechanics/mannequin/worm_2.png"
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

image worm:
    choice:
        "worm_1"
    choice:
        "worm_2"

transform worm_wiggle(s):
    xoffset 115*s
    zoom 0.0
    block:
        choice:
            yzoom 1.0
        choice:
            yzoom -1.0
    block:
        choice:
            xzoom 1.0
        choice:
            xzoom -1.0
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
    linear 0.15 zoom 1.35
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

screen mannequin_game(interactable=True):
    if not stitches_left and not stitches_right:
        timer 1.5 action Jump("mannequin_success")
    add "mannequin_background"
    add "mannequin_back" anchor (0.5, 0.5) pos back_pos
    add "open_scar" anchor (0.5, 0.5) pos open_scar_pos
    for i in range(1,6):
        use worm("left", i, interactable)
        use worm("right", i, interactable)
    add "open_scar_mask" anchor (0.5, 0.5) pos open_scar_mask_pos
    for i in range(1,6):
        use stitch("left", i, interactable)
        use stitch("right", i, interactable)
    use bandage("left", interactable)
    use bandage("right", interactable)
    for i in range(1,6):
        use top_stitch("left", i)
        use top_stitch("right", i)

screen worm(side, i, interactable=True):
    if not i in getattr(renpy.store, "stitches_%s" % side):
        imagebutton:
            at worm_wiggle(-1 if side == "right" else 1)
            focus_mask True
            if interactable:
                idle "worm"
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_cinch_%i_pos" % (side, i))
            action Jump("mannequin_fail")

# Could use some feedback like a hover or a cursor change
screen stitch(side, i, interactable=True):
    if i in getattr(renpy.store, "stitches_%s" % side):
        add "%s_cinch_%i" % (side, i):
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_cinch_%i_pos" % (side, i))
        imagebutton:
            # focus_mask True
            if interactable:
                action RemoveFromSet(getattr(renpy.store, "stitches_%s" % side), i)
            idle "%s_stitch_%i" % (side, i)
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_stitch_%i_pos" % (side, i))

screen top_stitch(side, i):
    if not i in getattr(renpy.store, "stitches_%s" % side):
        add "%s_stitch_%i" % (side, i) at stitch_pop(1 if side == "right" else -1):
            anchor (0.5, 0.5)
            pos getattr(renpy.store, "%s_stitch_%i_pos" % (side, i))

screen bandage(side, interactable=True):
    if getattr(renpy.store, "bandage_%s" % side):
        imagebutton:
            focus_mask True
            if interactable:
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
    show screen mannequin_game(False)
    call mannequin_intro
    call screen mannequin_game
    return
