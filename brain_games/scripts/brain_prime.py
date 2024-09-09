from brain_games.imports_for_scripts import welcome_user, start_game
from brain_games.games.prime import prime



def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game(name, prime)


if __name__ == "__main__":
    prime_game()
