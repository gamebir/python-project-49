from random import randint
BEGIN_RANGE = 1
END_RANGE = 10


def is_even(value):
    """parity check"""
    return 'yes' if value % 2 == 0 else 'no'


def brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = ''
    correct_answer = ''
    question = (randint(BEGIN_RANGE, END_RANGE))
    correct_answer = (is_even(question))
    return question, correct_answer, task