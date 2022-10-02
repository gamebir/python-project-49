#!/usr/bin/env python3
from brain_games.games import brain_prime
from brain_games.games_functions import engine_play


def main():
    engine_play(brain_prime.brain_prime, brain_prime.TASK)


if __name__ == "__main__":
    main()
