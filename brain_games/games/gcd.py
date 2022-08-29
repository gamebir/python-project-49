from random import randint
from brain_games.games_dialog import div, gr_com_div, greeting


def brain_gcd():
    name = greeting()
    print("Find the greatest common divisor of given numbers.")
    MAX_COuNT = 3
    count = 0
    while count < MAX_COuNT:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f"Question: {number1} {number2}")
        answer = int(input("Your answer:"))
        if answer == gr_com_div(div(number1), div(number2)):
            print("Correct!")
            count += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {gr_com_div(div(number1), div(number2))}. Let's try again, {name}")
            break
    if count == MAX_COuNT:
        print(f"Congratulations, {name}!")
