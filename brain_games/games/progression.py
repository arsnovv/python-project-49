import random
from brain_games.cli import welcome_user
from brain_games.games.start_games import start_game


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')

    def get_question_and_answer():
        num1 = random.randint(1, 100)
        num2 = random.randint(2, 5)
        i = 0
        progression_list = []
        while i < 10:
            i = i + 1
            num1 = num1 + num2
            progression_list.append(num1)

        random_index = random.randint(0, len(progression_list) - 1)
        correct_answer = progression_list[random_index]
        progression_list[random_index] = '..'

        question = f'Question: {' '.join(map(str, progression_list))}'
        return question, str(correct_answer)

    start_game(name, get_question_and_answer)
