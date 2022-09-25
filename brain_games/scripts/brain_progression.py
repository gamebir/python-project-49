#!/usr/bin/env python3
from brain_games.games.brain_progr import brain_progression, TASK
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_progression, TASK)


if __name__ == "__main__":
    main()
