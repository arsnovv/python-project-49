import random
import math


def gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'Question: {num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
