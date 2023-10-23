import random
from brain_games.game_logic import play_game

RULES = 'Find the greatest common divisor of given numbers.'


def prime_factors(num1, num2):
    """
    Find prime factorials for the number
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def gcd_game():
    questions = []
    answers = []

    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        questions.append(([str(num1) + ' ' + str(num2)]))
        answers.append(str(prime_factors(num1, num2)))

    play_game(questions, answers, RULES)
