from random import choice, randint


BEGIN_RANGE = 0
END_RANGE = 100
BEGIN_STEP = 3
END_STEP = 10
BEGIN_LENGHT = 10
END_LENGHT = 20
TASK = 'What number is missing in the progression?'


def generate_progression(step_progr, lenght_progr):
    """generating a sequence"""
    result = ''
    n = randint(BEGIN_RANGE, END_RANGE)
    for i in range(n, n + (step_progr * lenght_progr), step_progr):
        result += f'{i} '
    return result


def brain_progression():
    progression = generate_progression(randint(BEGIN_STEP, END_STEP), randint(BEGIN_LENGHT, END_LENGHT))
    symbol = choice(progression.split())
    question = progression.replace(symbol, '..')
    correct_answer = symbol
    return question, correct_answer
