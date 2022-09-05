from random import randint, choice
from brain_games.games_functions import greeting, math_action


MAX_COUNT = 3


def calc(max_count=MAX_COUNT):
    name = greeting()
    count = 0
    print("What is the result of the expression?")
    while count < max_count:
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
                f"\nLet's try again, {name}!"
            )
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}!")
