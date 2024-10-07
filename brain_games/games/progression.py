import random


def get_answer_and_question():
    length = 10
    start = random.randint(1, 100)
    step = random.randint(2, 5)
    stop = start + step * length

    progression_list = list(range(start, stop, step))

    random_index = random.randrange(length)
    correct_answer = progression_list[random_index]
    progression_list[random_index] = '..'

    question = ' '.join(map(str, progression_list))

    return question, str(correct_answer)
