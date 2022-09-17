from random import randint


def div(number):
    """list of divisors"""
    list_div = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_div.append(i)
    return list_div


def gr_com_div(list_div1, list_div2):
    """finding the greatest common divisor"""
    return max(set(list_div1) & set(list_div2))


def brain_gcd():
    task = 'Find the greatest common divisor of given numbers.'
    question = []
    rite_answer = []
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    rite_answer = str(gr_com_div(div(number1), div(number2)))
    return question, rite_answer, task
