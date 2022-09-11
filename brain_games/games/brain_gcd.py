from random import randint
from brain_games.games_functions import div, game_engine, gr_com_div, greeting


def brain_gcd():
    name = greeting()
    print("Find the greatest common divisor of given numbers.")
    question = []
    rite_answer = []
    for i in range(0, 3):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        question.append(f"{number1} {number2}")
        rite_answer.append(str(gr_com_div(div(number1), div(number2))))
    game_engine(question, rite_answer, name)
