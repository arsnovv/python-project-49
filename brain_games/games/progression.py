import random


def progression():
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
