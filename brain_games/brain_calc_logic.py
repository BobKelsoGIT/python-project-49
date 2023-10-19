import random
import prompt
from brain_games.general_func import welcome_user


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
    name = welcome_user()  # Greet the user
    for _ in range(3):  # Play 3 rounds
        expr = expression()
        print(f'What is the result of the expression?')
        print(f'Question: {expr}')
        answer = prompt.string(f'Your answer: ')  # Get user's answer
        right_answer = eval(expr)
        if int(answer) == right_answer:  # Check if the answer is correct
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            return
    print(f'Congratulations, {name}!')
