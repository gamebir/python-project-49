from random import randint
import prompt


def is_even(value):
    return bool(value % 2 )
    """проверка на четность"""


def games(question, answer):
    if not is_even(question) and answer == "yes":
        return True
    elif is_even(question) and answer == "no":
        return True
    elif not is_even(question) and answer == "no":
        return False
    elif is_even(question) and answer == "yes":
        return False
        """проверка ответа"""


def rev(answer):
    return "no" if answer == "yes" else "yes"
    """переворачиваем ответ"""


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n ")
    print(f"Hello, {name}")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    MAX_COUNT = 3
    count = 0
    while count < MAX_COUNT:
        question = randint(1, 10)
        print(f"Question: {question}")
        answer = input()
        if answer == "yes" or answer == "no":
            if games(question, answer):
                print(f"Your answer: {answer}\nCorrect!")
                count += 1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {rev(answer)}.\nLet's try again, {name}")
                break
            print(f"Congratulations, {name}!")
        else:
            break
greeting()
