import random
from brain_games.game_logic import play_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """
    Check if the given number is even.
    """
    return num % 2 == 0


def even_game():

    questions = []
    answers = []

    for _ in range(3):
        number = random.randint(1, 100)
        questions.append([str(number)])
        answers.append('yes' if is_even(number) else 'no')

    play_game(questions, answers, RULES)
