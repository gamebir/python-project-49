#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_calc.brain_calc, brain_calc.TASK)


if __name__ == "__main__":
    main()
