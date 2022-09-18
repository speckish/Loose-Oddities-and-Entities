define orb_item = "dog"
define orb_attempts = 3
define items = ["couch",
                "extension_cord",
                "poster",
                "cat",
                "dog",
                "fan",
                "picture",
                "vase"]

image orb_background = "mechanics/orb/background.png"
image orb_couch = "mechanics/orb/couch.png"
image orb_extension_cord = "mechanics/orb/extension_cord.png"
image orb_poster = "mechanics/orb/poster.png"
image orb_cat = "mechanics/orb/cat.png"
image orb_dog = "mechanics/orb/dog.png"
image orb_fan = "mechanics/orb/fan.png"
image orb_picture = "mechanics/orb/picture.png"
image orb_vase = "mechanics/orb/vase.png"

define orb_background_pos = (960, 540)
define orb_cat_pos = (364, 264)
define orb_dog_pos = (1512, 398)
define orb_vase_pos = (1402, 797)
define orb_couch_pos = (1062, 517)
define orb_picture_pos = (426, 763)
define orb_fan_pos = (587, 654)
define orb_extension_cord_pos = (1074, 860)
define orb_poster_pos = (956, 197)

screen orb_game():
    for i in items:
        use item(i)

screen item(i):
    imagebutton:
        idle "orb_%s" % i
        pos getattr(renpy.store, "orb_%s_pos" % i)
        action Confirm("Choose the %s?" % i, yes=[Return(i)])

label start_orb_game:
    jump orb_game_loop
    return

label orb_game_loop:
    call screen orb_game
    if orb_item == _return:
        jump orb_success
    else:
        $ orb_attempts -= 1
        if not orb_attempts:
            jump orb_fail
        else:
            call orb_incorrect(_return)
    jump orb_game_loop

label orb_incorrect(i):
    $ i_cap = i.capitalize()
    "[i_cap] was not what the orb wanted. Try again."
    return

label orb_success:
    "<You succeeded at the orb's task.>"
    jump end_game

label orb_fail:
    "<You failed the orb's task.>"
    jump end_game
