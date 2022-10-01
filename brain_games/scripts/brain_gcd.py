#!/usr/bin/env python3
from brain_games.games import brain_gcd
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_gcd.brain_gcd, brain_gcd.TASK)


if __name__ == "__main__":
    main()
