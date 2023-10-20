import random
from brain_games.game_logic import play_game


def is_even(num):
    """
    Check if the given number is even.
    """
    return num % 2 == 0


def even_game():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = []
    answers = []
    for _ in range(3):
        questions.append(random.randint(1, 100))
    for q in questions:
        if is_even(q):
            answers.append('yes')
        else:
            answers.append('no')

    play_game(questions, answers, description)
