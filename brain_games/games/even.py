import random
from brain_games.cli import welcome_user
from brain_games.games.start_games import start_game


def examination():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def get_question_and_answer():
        random_number = random.randint(1, 100)
        question = f'Question: {random_number}'
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        return question, correct_answer

    start_game(name, get_question_and_answer)
