#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.get_conditions_for_progression import (
    get_conditions_for_progression
)


def progression_game():
    name = welcome_user()
    print('What number is missing in the progression?')
    start_game(name, get_conditions_for_progression)


if __name__ == "__main__":
    progression_game()
