from random import randint
import prompt
from brain_games.games_functions import chec_answer, greeting, is_even, rev

MAX_COUNT = 3


def even(max_count=MAX_COUNT):
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < max_count:
        question = randint(1, 10)
        print(f"Question: {question}")
        question = is_even(question)
        answer = prompt.string("Your answer: ")
        if answer in ("yes", "no"):
            if chec_answer(question, answer):
                print("Correct!")
                count += 1
            else:
                print(
                    f""""{answer}"is wrong answer ;(. Correct answer was """
                    f""""{rev(answer)}".\nLet's try again, {name}!"""
                )
                break
        else:
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}!")
