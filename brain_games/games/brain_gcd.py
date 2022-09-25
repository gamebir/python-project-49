from random import randint
from math import gcd
BEGIN_RANGE = 1
END_RANGE = 100
TASK = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
    begin_range = BEGIN_RANGE
    end_range = END_RANGE
    question = ''
    correct_answer = ''
    first_value = randint(begin_range, end_range)
    second_value = randint(begin_range, end_range)
    question = f'{first_value} {second_value}'
    correct_answer = str(gcd(first_value, second_value))
    return question, correct_answer
