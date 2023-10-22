import random
from brain_games.game_logic import play_game


def is_prime(number):
    """
    Check if the number is ptime
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_game():

    DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    questions = []
    answers = []

    for _ in range(3):
        number = random.randint(1, 10)
        questions.append([str(number)])
        answers.append('yes' if is_prime(number) else 'no')

    play_game(questions, answers, DESCRIPTION)
