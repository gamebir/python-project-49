import prompt
from random import randint


def greeting():
    """greeting"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n")
    print(f"Hello, {name}")
    return name


def math_action(number1, number2, oper):
    """assign a mathematical operation to the symbol"""
    question = 0
    if oper == "+":
        question = number1 + number2
    elif oper == "-":
        question = number1 - number2
    elif oper == "*":
        question = number1 * number2
    return question


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


def gen_prog(step=3):
    """generating a sequence"""
    result = ""
    n = randint(0, 100)
    for i in range(n, n + (step * 10), step):
        result += f"{i} "
    return result


def is_prime_number(number):
    """check if the number is prime"""
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return "yes" if result == [1, number] else "no"


def is_even(value):
    """parity check"""
    return "yes" if value % 2 == 0 else "no"


def game_engine(question, rite_answer, name):
    """game engine"""
    MAX_COUNT = 3
    count = 0
    while count < MAX_COUNT:
        print(f"Question: {question[count]}")
        answer = prompt.string("Your answer: ")
        if rite_answer[count] == answer:
            print("Correct")
            count += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{rite_answer[count]}'.\nLet's try again, {name}!"
            )
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}!")
