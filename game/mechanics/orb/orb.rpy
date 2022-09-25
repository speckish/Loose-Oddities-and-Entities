define items = ["hat",
                "doll",
                "sewing_basket",
                "box",
                "album",
                "snowglobe",
                "towels",
                "beer",
                "spider",
                "bear",
                "blanket"]

image orb_background = "mechanics/orb/background.png"
image orb_bear = "mechanics/orb/bear.png"
image orb_blanket = "mechanics/orb/blanket.png"
image orb_box = "mechanics/orb/box.png"
image orb_doll = "mechanics/orb/doll.png"
image orb_hat = "mechanics/orb/hat.png"
image orb_sewing_basket = "mechanics/orb/sewing_basket.png"
image orb_snowglobe = "mechanics/orb/snowglobe.png"
image orb_spider = "mechanics/orb/spider.png"
image orb_towels = "mechanics/orb/towels.png"
image orb_album = "mechanics/orb/album.png"
image orb_beer = "mechanics/orb/beer.png"

define orb_hat_pos = (416, 143)
define orb_doll_pos = (677, 213)
define orb_sewing_basket_pos = (1126, 134)
define orb_box_pos = (1588, 127)
define orb_album_pos = (210, 611)
define orb_snowglobe_pos = (366, 728)
define orb_towels_pos = (797, 588)
define orb_beer_pos = (1259, 752)
define orb_spider_pos = (1647, 439)
define orb_bear_pos = (351, 1006)
define orb_blanket_pos = (1253, 1013)

transform orb_items:
    on idle:
        linear 0.25 matrixcolor TintMatrix("#ffffff")*SaturationMatrix(1.0)
    on hover:
        linear 0.25 matrixcolor TintMatrix("#ffffff")*SaturationMatrix(0.0)

screen orb_game(interactable=True):
    add "orb_background"
    for i in items:
        use item(i, interactable)

screen item(i, interactable=True):
    imagebutton:
        idle "orb_%s" % i
        pos getattr(renpy.store, "orb_%s_pos" % i)
        anchor (0.5, 0.5)
        if interactable:
            action Confirm("Choose the %s?" % i, yes=[Return(i)])
        at orb_items

label start_orb_game:
    show screen orb_game(False) with dissolve
    call orb_intro
    jump orb_game_loop
    return

label orb_game_loop:
    call screen orb_game
    if orb_item == _return:
        show screen orb_game(False)
        jump orb_success
    else:
        $ orb_attempts -= 1
        if not orb_attempts:
            show screen orb_game(False)
            call orb_fail(_return)
        else:
            show screen orb_game(False)
            call orb_incorrect(_return)
    jump orb_game_loop
