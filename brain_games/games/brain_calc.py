from random import randint, choice
from brain_games.games_functions import game_engine, greeting


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


def brain_calc(task='What is the result of the expression?'):
    question = []
    rite_answer = []
    for i in range(0, 3):
        oper = choice(['+', '-', '*'])
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        question.append(f"{number1} {oper} {number2}")
        rite_answer.append(str(math_action(number1, number2, oper)))
    game_engine(question, rite_answer, task)
