
image black = "#000"

label end_game:
    $ renpy.full_restart()

label test_mechanics:
    menu:
        "Doll":
            jump start_doll_game
        "Mannequin":
            jump start_mannequin_game
        "Woman":
            jump start_woman_game
        "Cards":
            jump start_cards_game
        "Horned":
            jump start_horned_game
        "Orb":
            jump start_orb_game
