from random import randint
from brain_games.games_functions import div, gr_com_div, greeting, is_digit

MAX_COUNT = 3


def brain_gcd(max_count=MAX_COUNT):
    name = greeting()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count < max_count:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f"Question: {number1} {number2}")
        answer = is_digit("Your answer:")
        if answer == gr_com_div(div(number1), div(number2)):
            print("Correct!")
            count += 1
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was "
                f"{gr_com_div(div(number1), div(number2))}. "
                f"Let's try again, {name}!"
            )
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}!")
