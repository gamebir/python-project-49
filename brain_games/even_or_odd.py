from random import randint
import prompt


# проверка на четность
def even(value):
    return True if not value % 2 else False


# проверка ответа
def games(question, answer):
    if even(question) is True and answer == "yes":
        return True
    elif even(question) is False and answer == "no":
        return True
    elif even(question) is True and answer == "no":
        return False
    elif even(question) is False and answer == "yes":
        return False


# переворачиваем ответ
def rev(answer):
    return "no" if answer == "yes" else "yes"


# диалог
def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n ")
    print(f"Hello, {name}")
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    count = 0
    while count < 3:
        question = randint(1, 10)
        print(f"Question: {question}")
        answer = input()
        if answer == "yes" or answer == "no":
            if games(question, answer) is True:
                print(f"Your answer: {answer}\nCorrect!")
                count += 1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer/"
                    "was {rev(answer)}.\nLet's try again, {name}")
                break
            print(f"Congratulations, {name}!")
        else:
            break
