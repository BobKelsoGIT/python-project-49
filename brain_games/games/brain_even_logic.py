import random
import prompt
from brain_games.general_func import welcome_user


def is_even(num):
    """
    Check if the given number is even.
    """
    return num % 2 == 0


def even_game():
    """
    Play a game where the user needs to guess if a number is even or not.
    """
    name = welcome_user()  # Greet the user
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):  # Play 3 rounds
        num = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(f'Question: {num}')  # Display the question
        answer = prompt.string('Your answer: ')  # Get user's answer

        if answer == 'yes' and is_even(num) or answer == 'no' and not is_even(num):  # Check if the answer is correct
            print('Correct!')
        else:
            if is_even(num):
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
