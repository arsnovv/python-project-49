import random
import operator


def get_answer_and_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]

    sign, result = random.choice(operations)
    question = f'{num1} {sign} {num2}'
    correct_answer = str(result(num1, num2))

    return question, correct_answer
