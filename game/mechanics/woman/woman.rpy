# Customizable variables
define woman_length = 30.0 # Length of the game in seconds.
define woman_frequency_min = 2.5 # Minimum time between prompts.
define woman_frquency_max = 3.5 # Maximum time between prompts.
define woman_prompt_timeout = 2.0 # Time you have to respond to a prompt before you make a noise.
define woman_chances = 1 # Number of times the woman will let you slip up before you're killed. In the actual game this will be determined by whether or not the woman likes you.
# Customizable variables end here.

define woman_keys = "1234567890"

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
        jump start_woman_game
    else:
        jump woman_bad_end
    return

label woman_bad_end:
    hide screen qte_prompt
    "woman" "I told you to be quiet!"
    return

label woman_success:
    hide screen qte_prompt
    "woman" "You made it! Guesss I won't have to kill you~"
    return

label start_woman_game:
    call screen woman_game
    return
