#!/usr/bin/env python3
from brain_games.games.brain_even import brain_even, TASK
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_even, TASK)


if __name__ == "__main__":
    main()
