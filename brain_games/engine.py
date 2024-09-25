
def start_game(name, get_question_and_answer):
    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")
