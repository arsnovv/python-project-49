
def start_game(name, get_question_and_answer):
    i = 0
    while i < 3:
        question, correct_answer = get_question_and_answer()
        print(question)
        answer = input('Your answer: ')
        if answer == correct_answer:
            i += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
