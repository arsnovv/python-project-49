#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.even import examination


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(name, examination)


if __name__ == "__main__":
    even_game()
