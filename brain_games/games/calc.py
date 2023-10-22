import random
from brain_games.game_logic import play_game


def expression():
    """
    Generating expression
    """
    list_of_expressions = ['+', '-', '*']
    first_number = random.randint(1, 10)  # generating first Int
    second_number = random.randint(1, 10)  # generating second Int
    operator = random.choice(list_of_expressions)  # pick '+', '-' or '*' randomly
    return f'{first_number} {operator} {second_number}'  # return generated expression


def calc_game():
    """
    Play a game where the user needs to calculate the expression
    """
    DESCRIPTION = 'What is the result of the expression?'

    questions = []
    answers = []
    for _ in range(3):
        questions.append([expression()])

    for q in questions:
        for i in q:
            answers.append(str(eval(i)))

    play_game(questions, answers, DESCRIPTION)
