import random
import prompt
def examination():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        x = input('Your answer:')
        if random_number % 2 == 0:
            if x == "yes":
                i = i + 1
                print('Correct!')
            else:
                i = 4
                print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again," + name + '!')
        if random_number % 2 != 0:
            if x == "no":
                i = i + 1
                print('Correct!')
            else:
                i = 4
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again," + name + '!')
        if i == 3:
            print('Congratulations,'+ name + '!')