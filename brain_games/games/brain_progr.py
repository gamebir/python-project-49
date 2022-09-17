from random import choice, randint


def gen_prog(step=3):
    """generating a sequence"""
    result = ''
    n = randint(0, 100)
    for i in range(n, n + (step * 10), step):
        result += f'{i} '
    return result


def brain_progr():
    task = 'What number is missing in the progression?'
    question = []
    rite_answer = []
    prog = gen_prog()
    simbol = choice(prog.split())
    question = prog.replace(simbol, '..')
    rite_answer = simbol
    return question, rite_answer, task
