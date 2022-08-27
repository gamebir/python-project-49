import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n ")
    print(f"Hello, {name}")
    return name
    """приветствие"""


def rev(answer):
    return "no" if answer == "yes" else "yes"
    """переворачиваем ответ"""


def math_action(number1, number2, oper):
    question = 0
    if oper == "+":
        question = number1 + number2
    elif oper == "-":
        question = number1 - number2
    elif oper == "*":
        question = number1 * number2
    return question
