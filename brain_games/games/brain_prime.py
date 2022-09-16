from random import randint
from brain_games.games_functions import game_engine, greeting


def is_prime_number(number):
    """check if the number is prime"""
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return 'yes' if result == [1, number] else 'no'


def brain_prime():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question = []
    rite_answer = []
    for i in range(0, 3):
        question.append(randint(1, 223))
        rite_answer.append(is_prime_number(question[i]))
    game_engine(question, rite_answer, name)
