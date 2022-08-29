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
    """Присваеваем символу математическую операцию"""


def div(number):
    list_div = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_div.append(i)
    return list_div
    """список делителей"""


def gr_com_div(list_div1, list_div2):
    return max(set(list_div1) & set(list_div2))
    """поиск наибольшего общего делителя"""
