#!/usr/bin/env python3
from brain_games.games.brain_calc import brain_calc, TASK
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_calc, TASK)


if __name__ == "__main__":
    main()
