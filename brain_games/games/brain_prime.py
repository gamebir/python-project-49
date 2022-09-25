from random import randint
BEGIN_RANGE = 1
END_RANGE = 223
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    """check if the number is prime"""
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return True if result == [1, number] else False


def brain_prime():
    begin_range = BEGIN_RANGE
    end_range = END_RANGE
    question = ''
    correct_answer = ''
    question = randint(begin_range, end_range)
    if is_prime_number(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
