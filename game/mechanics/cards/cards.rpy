# Customizable variables.
define cards_num_cards = 3 # How many cards are splayed at once.
define cards_padding = 300
# Customizable variables end here.

default cards_selected = None

image card_back = "mechanics/cards/card_back.png"
image card_front_good = "mechanics/cards/card_front_good.png"
image card_front_bad = "mechanics/cards/card_front_bad.png"

transform card_spacer:
    alpha 0.01

transform card_slide_in(i):
    anchor (0.5, 1.0)
    pos (0.5, 0.0)
    rotate 180
    linear 1.5 yalign 0.5
    pause 0.5
    parallel:
        linear 1.5 rotate 0
    parallel:
        linear 1.5 offset (int(-config.screen_width/2)+int(cards_padding+(config.screen_width-cards_padding*2)/(cards_num_cards-1.0)*i), 0)

transform card(i):
    anchor (0.5, 0.5)
    pos (int(cards_padding+(config.screen_width-cards_padding*2)/(cards_num_cards-1.0)*i), 0.5)
    on idle:
        linear 0.35 rotate 0
    on hover:
        parallel:
            linear 0.5 yoffset 0
        parallel:
            linear 0.25 rotate 5
            block:
                linear 0.5 rotate -10
                linear 0.5 rotate 10
                repeat

transform card_wiggle:
    on idle:
        linear 0.25 yoffset -5
        block:
            linear 0.5 yoffset 10
            linear 0.5 yoffset -10
            repeat

transform card_back_down:
    xzoom 1.0

transform card_front_down:
    xzoom 0.0

transform card_flip_up:
    anchor (0.5, 0.5)
    linear 0.5 zoom 1.25
    pause 0.5
    linear 0.5 zoom 1.0

transform card_back_flip_up:
    align (0.5, 0.5)
    pause 0.5
    linear 0.25 xzoom 0.0

transform card_front_flip_up:
    align (0.5, 0.5)
    xzoom 0.0
    pause 0.75
    linear 0.25 xzoom 1.0

screen cards_game(cards):
    tag cards
    for i in range(len(cards)):
        use card(cards[i], i)

screen deal_cards(cards):
    for i in range(len(cards)):
        use deal_card(cards[i], i)

screen reveal_cards(cards):
    tag cards
    for i in range(len(cards)):
        if i == cards_selected:
            use reveal_card(cards[i], i)
        else:
            use card(cards[i], i, False)

screen card(c, i, w=True):
    default card_front = "card_front_bad" if not c else "card_front_good"
    button:
        action [SetVariable("cards_selected", i), Return()]
        at card(i)
        fixed:
            if c and w:
                at card_wiggle
            fit_first True
            add "card_back" at card_spacer
            add "card_back" at card_back_down
            add card_front at card_front_down

screen deal_card(c, i):
    tag cards
    default card_front = "card_front_bad" if not c else "card_front_good"
    fixed:
        at card_slide_in(i)
        fit_first True
        add "card_back" at card_spacer
        add "card_back" at card_back_down
        add card_front at card_front_down

screen reveal_card(c, i):
    tag cards
    default card_front = "card_front_bad" if not c else "card_front_good"
    fixed:
        at card(i), card_flip_up
        fit_first True
        add "card_back" at card_spacer
        add "card_back" at card_back_flip_up
        add card_front at card_front_flip_up

label start_cards_game:
    window hide
    $ card_selected = False
    $ cards = [None for i in range(cards_num_cards-1)]
    $ cards.append(True)
    $ random.shuffle(cards)
    show screen deal_cards(cards)
    pause 3.5
    "Now, pick, and pick correctly or else!"
    hide screen deal_cards
    call screen cards_game(cards)
    # window hide
    show screen reveal_cards(cards)
    pause 1.0
    if cards[cards_selected]:
        "Lucky guess. You pass for now."
        jump end_game
    else:
        "OOHHH, so close...but not close enough. Guess you die now!"
        jump end_game
    return
