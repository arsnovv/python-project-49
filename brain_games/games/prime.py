import random
import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def prime():
    random_number = random.randint(1, 100)
    question = f'Question: {random_number}'
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer
