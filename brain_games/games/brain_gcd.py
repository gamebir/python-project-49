from random import randint
from math import gcd
BEGIN_RANGE = 1
END_RANGE = 100


def brain_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    question = ''
    correct_answer = ''
    number1 = randint(BEGIN_RANGE, END_RANGE)
    number2 = randint(BEGIN_RANGE, END_RANGE)
    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer, task
