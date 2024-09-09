#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.prime import prime


def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game(name, prime)


if __name__ == "__main__":
    prime_game()
