from random import choice
from brain_games.games_functions import gen_prog, greeting, is_digit


MAX_COUNT = 3


def brain_progr(max_count=MAX_COUNT):
    name = greeting()
    print("What number is missing in the progression?")
    count = 0
    while count < max_count:
        prog = gen_prog()
        simbol = choice(prog.split())
        question = prog.replace(simbol, "..")
        print(f"Question: {question}")
        answer = is_digit("Your answer: ")
        if int(simbol) == answer:
            print("Correct!")
            count += 1
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was {simbol}."
                f"\nLet's try again, {name}!"
            )
            break
    if MAX_COUNT == count:
        print(f"Congratulations, {name}!")
