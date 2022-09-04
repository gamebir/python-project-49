from random import randint
import prompt
from brain_games.games_functions import chech_answer, greeting, is_even, rev


def even(MAX_COUNT=3):
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < MAX_COUNT:
        question = randint(1, 10)
        print(f"Question: {question}")
        question = is_even(question)
        answer = prompt.string("Your answer: ")
        if answer in ("yes", "no"):
            if chech_answer(question, answer):
                print("Correct!")
                count += 1
            else:
                print(
                    f"{answer} is wrong answer ;(. Correct answer was "
                    f"{rev(answer)}.\nLet's try again, {name}"
                )
                break
        else:
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}")
