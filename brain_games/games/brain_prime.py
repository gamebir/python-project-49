from random import randint


def is_prime_number(number):
    """check if the number is prime"""
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return 'yes' if result == [1, number] else 'no'


def brain_prime():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = []
    rite_answer = []
    question = randint(1, 223)
    rite_answer = is_prime_number(question)
    return question, rite_answer, task
