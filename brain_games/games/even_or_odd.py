from random import randint
from brain_games.games_dialog import greeting, rev



def is_odd(value):
    return bool(value % 2)
    """проверка на четность"""


def games(question, answer):
    if not is_odd(question) and answer == "yes":
        return True
    elif is_odd(question) and answer == "no":
        return True
    elif not is_odd(question) and answer == "no":
        return False
    elif is_odd(question) and answer == "yes":
        return False
        """проверка ответа"""


def even(MAX_COUNT = 3):
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < MAX_COUNT:
        question = randint(1, 10)
        print(f"Question: {question}")
        answer = input()
        if answer in ("yes", "no"):
            if games(question, answer):
                print(f"Your answer: {answer}\nCorrect!")
                count += 1
            else:
                print(
                    f"{answer} is wrong answer ;(. Correct answer was {rev(answer)}.\nLet's try again, {name}"
                )
                break
            print(f"Congratulations, {name}!")
        else:
            break
