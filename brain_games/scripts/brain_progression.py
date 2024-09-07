#!/usr/bin/env python3
from brain_games.games.progression import progression
from brain_games.cli import welcome_user
from brain_games.engine import start_game


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    start_game(name, progression)


if __name__ == "__main__":
    main()
