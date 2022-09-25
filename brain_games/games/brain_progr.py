from random import choice, randint
BEGIN_RANGE = 2
END_RANGE = 10
BEGIN_RANGE_2 = 0
END_RANGE_2 = 100
PROGR_LENGHT = 10
TASK = 'What number is missing in the progression?'


def gen_prog():
    """generating a sequence"""
    begin_range = BEGIN_RANGE
    end_range = END_RANGE
    begin_range_2 = BEGIN_RANGE_2
    end_range_2 = END_RANGE_2
    progr_lenght = PROGR_LENGHT
    step = randint(begin_range, end_range)
    result = ''
    n = randint(begin_range_2, end_range_2)
    for i in range(n, n + (step * progr_lenght), step):
        result += f'{i} '
    return result


def brain_progression():
    question = ''
    correct_answer = ''
    progression = gen_prog()
    symbol = choice(progression.split())
    question = progression.replace(symbol, '..')
    correct_answer = symbol
    return question, correct_answer
