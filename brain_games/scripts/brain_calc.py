#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.calc import get_answer_and_question


def calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    start_game(name, get_answer_and_question)


if __name__ == "__main__":
    calc_game()
