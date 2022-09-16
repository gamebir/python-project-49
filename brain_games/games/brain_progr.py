from random import choice, randint
from brain_games.games_functions import game_engine, greeting


def gen_prog(step=3):
    """generating a sequence"""
    result = ''
    n = randint(0, 100)
    for i in range(n, n + (step * 10), step):
        result += f'{i} '
    return result


def brain_progr():
    name = greeting()
    print('What number is missing in the progression?')
    question = []
    rite_answer = []
    for i in range(0, 3):
        prog = gen_prog()
        simbol = choice(prog.split())
        question.append(prog.replace(simbol, '..'))
        rite_answer.append(simbol)
    game_engine(question, rite_answer, name)
