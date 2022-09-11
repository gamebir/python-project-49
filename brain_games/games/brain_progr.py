from random import choice
from brain_games.games_functions import game_engine, gen_prog, greeting


def brain_progr():
    name = greeting()
    print("What number is missing in the progression?")
    question = []
    rite_answer = []
    for i in range(0, 3):
        prog = gen_prog()
        simbol = choice(prog.split())
        question.append(prog.replace(simbol, ".."))
        rite_answer.append(simbol)
    game_engine(question, rite_answer, name)
