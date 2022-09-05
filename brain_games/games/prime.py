from random import randint
import prompt
from brain_games.games_functions import chec_answer, greeting
from brain_games.games_functions import is_prime_number, rev

MAX_COUNT = 3


def brain_prime(max_count=MAX_COUNT):
    name = greeting()
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count < max_count:
        question = randint(1, 223)
        print(f"Question: {question}")
        question = is_prime_number(question)
        answer = prompt.string("Your answer: ")
        if chec_answer(question, answer):
            print("Correct!")
            count += 1
        else:
            print(
                f""""{answer}" is wrong answer ;(. Correct answer was"""
                f""" "{rev(answer)}".\nLet's try again, {name}!"""
            )
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}!")
