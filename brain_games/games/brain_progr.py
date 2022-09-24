from random import choice, randint
BEGIN_RANGE = 2
END_RANGE = 10
BEGIN_RANGE_2 = 0
END_RANGE_2 = 100
PROGR_LENGHT = 10


def gen_prog():
    """generating a sequence"""
    step = randint(BEGIN_RANGE,END_RANGE)
    result = ''
    n = randint(BEGIN_RANGE_2, END_RANGE_2)
    for i in range(n, n + (step * PROGR_LENGHT), step):
        result += f'{i} '
    return result


def brain_progr():
    task = 'What number is missing in the progression?'
    question = ''
    correct_answer = ''
    progression = gen_prog()
    symbol = choice(progression.split())
    question = progression.replace(symbol, '..')
    correct_answer = symbol
    return question, correct_answer, task
print(gen_prog())
