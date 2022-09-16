from random import randint
from brain_games.games_functions import game_engine, greeting


def div(number):
    """list of divisors"""
    list_div = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_div.append(i)
    return list_div


def gr_com_div(list_div1, list_div2):
    """finding the greatest common divisor"""
    return max(set(list_div1) & set(list_div2))


def brain_gcd():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    question = []
    rite_answer = []
    for i in range(0, 3):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        question.append(f'{number1} {number2}')
        rite_answer.append(str(gr_com_div(div(number1), div(number2))))
    game_engine(question, rite_answer, name)
