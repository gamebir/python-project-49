from random import randint, choice
BEGIN_RANGE = 1
END_RANGE = 10


def math_action(number1, number2, oper):
    """assign a mathematical operation to the symbol"""
    operation_result = 0
    if oper == '+':
        operation_result = number1 + number2
    elif oper == '-':
        operation_result = number1 - number2
    elif oper == '*':
        operation_result = number1 * number2
    return operation_result


def brain_calc():
    task = 'What is the result of the expression?'
    question = ''
    correct_answer = ''
    oper = choice(['+', '-', '*'])
    number1 = randint(BEGIN_RANGE, END_RANGE)
    number2 = randint(BEGIN_RANGE, END_RANGE)
    question = (f'{number1} {oper} {number2}')
    correct_answer = (str(math_action(number1, number2, oper)))
    return question, correct_answer, task
