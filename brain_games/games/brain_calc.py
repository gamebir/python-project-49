from random import randint, choice
BEGIN_RANGE = 1
END_RANGE = 10
TASK = 'What is the result of the expression?'


def math_action(first_value, second_value, operator):
    """assign a mathematical operation to the symbol"""
    operation_result = 0
    if operator == '+':
        operation_result = first_value + second_value
    elif operator == '-':
        operation_result = first_value - second_value
    elif operator == '*':
        operation_result = first_value * second_value
    return operation_result


def brain_calc():
    begin_range = BEGIN_RANGE
    end_range = END_RANGE
    question = ''
    correct_answer = ''
    operator = choice(['+', '-', '*'])
    first_value = randint(begin_range, end_range)
    second_value = randint(begin_range, end_range)
    question = (f'{first_value} {operator} {second_value}')
    correct_answer = (str(math_action(first_value, second_value, operator)))
    return question, correct_answer
