from random import randint
BEGIN_RANGE = 1
END_RANGE = 10
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    """parity check"""
    return 'yes' if value % 2 == 0 else 'no'


def brain_even():
    begin_range = BEGIN_RANGE
    end_range = END_RANGE
    question = ''
    correct_answer = ''
    question = (randint(begin_range, end_range))
    correct_answer = (is_even(question))
    return question, correct_answer
