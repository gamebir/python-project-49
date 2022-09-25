#!/usr/bin/env python3
from brain_games.games.brain_prime import brain_prime, TASK
from brain_games.games_functions import game_engine


def main():
    game_engine(brain_prime, TASK)


if __name__ == "__main__":
    main()
