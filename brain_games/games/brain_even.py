from random import randint


def is_even(value):
    """parity check"""
    return 'yes' if value % 2 == 0 else 'no'


def brain_even():
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = []
    rite_answer = []
    question = (randint(1, 10))
    rite_answer = (is_even(question))
    return question, rite_answer, task
