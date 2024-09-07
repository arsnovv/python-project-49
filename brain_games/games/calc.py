import random


def calc():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    opera = random.choice(['+', '-', '*'])
    question = f'Question: {num1} {opera} {num2}'
    correct_answer = str(eval(f'{num1} {opera} {num2}'))
    return question, correct_answer
