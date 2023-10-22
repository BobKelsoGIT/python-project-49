import random
from brain_games.game_logic import play_game


def prime_factors(number):
    i = 2
    factors = []
    while i * i <= number:
        while number % i == 0:
            factors.append(i)
            number = number / i
        i = i + 1
    if number > 1:
        factors.append(number)
    return factors


def gcd_game():
    description = 'Find the greatest common divisor of given numbers.'
    numbers_for_calculations = []
    questions = []
    answers = []

    for _ in range(3):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        numbers_for_calculations.append([first_number, second_number])
        questions.append(([str(first_number) + ' ' + str(second_number)]))

    for q in numbers_for_calculations:
        list_of_prime_factors = [str(round(value)) for value in prime_factors(q[0]) if value in prime_factors(q[1])]
        if list_of_prime_factors:
            answers.append(str(max(list_of_prime_factors)))
        else:
            answers.append(str(1))

    play_game(questions, answers, description)
