#!/usr/bin/env python3
from brain_games.games import brain_progr
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_progr.brain_progression, brain_progr.TASK)


if __name__ == "__main__":
    main()
