from brain_games.imports_for_scripts import welcome_user, start_game
from brain_games.games.calc import calc



def calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    start_game(name, calc)


if __name__ == "__main__":
    calc_game()
