from random import randint
from brain_games.games_functions import game_engine, greeting, is_prime_number


def brain_prime():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question = []
    rite_answer = []
    for i in range(0, 3):
        question.append(randint(1, 223))
        rite_answer.append(is_prime_number(question[i]))
    game_engine(question, rite_answer, name)
