from brain_games.imports_for_scripts import welcome_user, start_game
from brain_games.games.progression import progression



def progression_game():
    name = welcome_user()
    print('What number is missing in the progression?')
    start_game(name, progression)


if __name__ == "__main__":
    progression_game()
