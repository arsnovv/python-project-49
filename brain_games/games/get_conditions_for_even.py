import random


def get_conditions_for_examination():
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return question, correct_answer
