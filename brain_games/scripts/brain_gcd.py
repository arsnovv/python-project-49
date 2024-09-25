#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.engine import start_game
from brain_games.games.gcd import get_answer_and_question


def gcd_game():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    start_game(name, get_answer_and_question)


if __name__ == "__main__":
    gcd_game()
