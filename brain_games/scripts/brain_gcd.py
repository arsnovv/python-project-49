#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.cli import welcome_user
from brain_games.engine import start_game


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    start_game(name, gcd)


if __name__ == "__main__":
    main()
