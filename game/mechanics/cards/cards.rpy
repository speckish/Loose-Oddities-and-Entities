define cards_num_cards = 3 # How many cards are splayed at once.
define cards_padding = 300
default cards_selected = None

image card_back = "mechanics/cards/card_back.png"
image card_front_good = "mechanics/cards/card_front_good.png"
image card_front_bad = "mechanics/cards/card_front_bad.png"
image card_front_neutral = "mechanics/cards/card_front_neutral.png"

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
        use card(cards[i], i, True)

screen deal_cards(cards):
    for i in range(len(cards)):
        use deal_card(cards[i], i)

screen reveal_cards(cards):
    tag cards
    for i in range(len(cards)):
        if i == cards_selected:
            use reveal_card(cards[i], i)
        else:
            use card(cards[i], i)

screen card(c, i, w=False):
    default card_front = "card_front_%s" % c
    button:
        if w:
            action [SetVariable("cards_selected", i), Return()]
        at card(i)
        fixed:
            if c == cards_desired_card and w:
                at card_wiggle
            fit_first True
            add "card_back" at card_spacer
            add "card_back" at card_back_down
            add card_front at card_front_down

screen deal_card(c, i):
    tag cards
    default card_front = "card_front_%s" % c
    fixed:
        at card_slide_in(i)
        fit_first True
        add "card_back" at card_spacer
        add "card_back" at card_back_down
        add card_front at card_front_down

screen reveal_card(c, i):
    tag cards
    default card_front = "card_front_%s" % c
    fixed:
        at card(i), card_flip_up
        fit_first True
        add "card_back" at card_spacer
        add "card_back" at card_back_flip_up
        add card_front at card_front_flip_up

label start_cards_game:
    window hide
    $ card_selected = False
    $ cards = ["good", "bad", "neutral"]
    $ random.shuffle(cards)
    show screen deal_cards(cards)
    pause 3.85
    call cards_intro
    hide screen deal_cards
    call screen cards_game(cards)
    # window hide
    show screen reveal_cards(cards)
    pause 1.0
    call expression "cards_picked_%s_card" % cards[cards_selected]
    return
