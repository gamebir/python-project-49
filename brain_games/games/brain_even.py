from random import randint
from brain_games.games_functions import game_engine, greeting, is_even


def brain_even():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = []
    rite_answer = []
    for i in range(0, 3):
        question.append(randint(1, 10))
        rite_answer.append(is_even(question[i]))
    game_engine(question, rite_answer, name)
