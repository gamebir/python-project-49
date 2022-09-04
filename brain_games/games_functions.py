import prompt
from random import randint


def greeting():
    """приветствие"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n")
    print(f"Hello, {name}")
    return name


def rev(answer):
    """переворачиваем ответ"""
    return "no" if answer == "yes" else "yes"


def math_action(number1, number2, oper):
    """Присваеваем символу математическую операцию"""
    question = 0
    if oper == "+":
        question = number1 + number2
    elif oper == "-":
        question = number1 - number2
    elif oper == "*":
        question = number1 * number2
    return question


def div(number):
    """список делителей"""
    list_div = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_div.append(i)
    return list_div


def gr_com_div(list_div1, list_div2):
    """поиск наибольшего общего делителя"""
    return max(set(list_div1) & set(list_div2))


def is_digit(text):
    """проверка на число"""
    value = input(text)
    return int(value) if value.isdigit() else is_digit(text)


def gen_prog(step=3):
    """генерируем последовательность"""
    result = ""
    n = randint(0, 100)
    for i in range(n, n + (step * 10), step):
        result += f"{i} "
    return result


def is_prime_number(number):
    """проверяем является ли число простым"""
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return True if result == [1, number] else False


def chech_answer(question, answer):
    """проверка ответа"""
    if question and answer == "yes" or not question and answer == "no":
        return True
    elif not question and answer == "yes" or question and answer == "no":
        return False


def is_even(value):
    """проверка на четность"""
    return not bool(value % 2)
