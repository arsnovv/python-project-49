from brain_games.imports_for_scripts import welcome_user, start_game
from brain_games.games.even import examination



def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(name, examination)


if __name__ == "__main__":
    even_game()
