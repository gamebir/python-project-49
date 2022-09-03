from random import randint
import prompt
from brain_games.games_functions import chech_answer, greeting, is_prime_number, rev


def brain_prime(MAX_COUNT=3):
    name = greeting()
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count < MAX_COUNT:
        question = randint(1, 223)
        print(f"Question: {question}")
        question = is_prime_number(question)
        answer = prompt.string("Your answer: ")
        if chech_answer(question, answer):
            print("Correct!")
            count += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {rev(answer)}.\nLet's try again, {name}")
            break
    if count == MAX_COUNT:
        print(f"Congratulations, {name}!")
