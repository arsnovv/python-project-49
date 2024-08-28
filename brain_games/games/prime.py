import random
import math
from brain_games.cli import welcome_user
from brain_games.games.start_games import start_game


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def get_question_and_answer():
        random_number = random.randint(1, 100)
        question = f'Question: {random_number}'
        correct_answer = 'yes' if is_prime(random_number) else 'no'
        return question, correct_answer

    start_game(name, get_question_and_answer)
