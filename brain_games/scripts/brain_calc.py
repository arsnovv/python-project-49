#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.get_conditions_for_calc import get_conditions_for_calc


def calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    start_game(name, get_conditions_for_calc)


if __name__ == "__main__":
    calc_game()
