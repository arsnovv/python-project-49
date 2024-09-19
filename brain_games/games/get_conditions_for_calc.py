import random


def calculate(num1, num2, opera):
    if opera == '+':
        return num1 + num2
    elif opera == '-':
        return num1 - num2
    elif opera == '*':
        return num1 * num2


def get_conditions_for_calc():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    opera = random.choice(['+', '-', '*'])
    question = f'{num1} {opera} {num2}'
    correct_answer = str(calculate(num1, num2, opera))
    return question, correct_answer
