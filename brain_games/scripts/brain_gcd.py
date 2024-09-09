from brain_games.imports_for_scripts import welcome_user, start_game
from brain_games.games.gcd import gcd



def gcd_game():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    start_game(name, gcd)


if __name__ == "__main__":
    gcd_game()
