import random
import prompt
from brain_games.cli import welcome_user
from brain_games.games.start_games import start_game

def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    def get_question_and_answer():
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        opera = random.choice(['+', '-', '*'])
        question = f'Question: {num1} {opera} {num2}'
        correct_answer = str(eval(f'{num1} {opera} {num2}'))
        return question, correct_answer

    start_game(name, get_question_and_answer)