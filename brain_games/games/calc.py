import random
from brain_games.game_logic import play_game

RULES = 'What is the result of the expression?'


def expression():
    """
    Generating expression
    """
    list_of_expressions = ['+', '-', '*']
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(list_of_expressions)
    return f'{first_number} {operator} {second_number}'


def calc_game():
    questions = []
    answers = []
    for _ in range(3):
        questions.append([expression()])

    for q in questions:
        for i in q:
            answers.append(str(eval(i)))

    play_game(questions, answers, RULES)
