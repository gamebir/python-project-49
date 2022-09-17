from random import randint, choice


def math_action(number1, number2, oper):
    """assign a mathematical operation to the symbol"""
    question = 0
    if oper == '+':
        question = number1 + number2
    elif oper == '-':
        question = number1 - number2
    elif oper == '*':
        question = number1 * number2
    return question


def brain_calc():
    task = 'What is the result of the expression?'
    question = []
    rite_answer = []
    oper = choice(['+', '-', '*'])
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    question = (f"{number1} {oper} {number2}")
    rite_answer = (str(math_action(number1, number2, oper)))
    return question, rite_answer, task
