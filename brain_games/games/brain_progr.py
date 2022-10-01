from random import choice, randint


BEGIN_RANGE = 0
END_RANGE = 100
STEP_PROGR = 3
LEGHT_PROGR = 10
TASK = 'What number is missing in the progression?'


def generate_progression(step_progr, leght_progr):
    """generating a sequence"""
    result = ''
    n = randint(BEGIN_RANGE, END_RANGE)
    for i in range(n, n + (step_progr * leght_progr), step_progr):
        result += f'{i} '
    return result


def brain_progression():
    progression = generate_progression(STEP_PROGR, LEGHT_PROGR)
    symbol = choice(progression.split())
    question = progression.replace(symbol, '..')
    correct_answer = symbol
    return question, correct_answer
