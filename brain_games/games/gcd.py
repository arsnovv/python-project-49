import random
import math
from brain_games.cli import welcome_user
from brain_games.games.start_games import start_game


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    def get_question_and_answer():
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f'Question: {num1} {num2}'
        correct_answer = str(math.gcd(num1, num2))
        return question, correct_answer

    start_game(name, get_question_and_answer)
