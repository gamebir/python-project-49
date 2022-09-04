from random import randint, choice
from brain_games.games_functions import greeting, is_digit, math_action


def calc(MAX_COUNT=3):
    name = greeting()
    count = 0
    print("What is the result of the expression?")
    while count < MAX_COUNT:
        oper = choice(["+", "-", "*"])
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        print(f"Question: {number1} {oper} {number2}")
        answer = int(input("Your answer: "))
        question = math_action(number1, number2, oper)
        if question == answer:
            print("Correct!")
            count += 1
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was {question}."
                f"\nLet's try again, {name}"
            )
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}")
