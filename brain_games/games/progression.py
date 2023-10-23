import random
from brain_games.game_logic import play_game

RULES = 'What number is missing in the progression?'


def generate_progression() -> list:
    """
    Generate the progression
    """
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    return [str(start + i * step) for i in range(length)]


def generate_question(progression):
    """
    Generate a question
    """
    index_to_replace = random.randint(0, len(progression) - 1)
    correct_answer = progression[index_to_replace]
    progression[index_to_replace] = '..'
    return progression, correct_answer


def generate_game_data():
    """
    Generate the list of questions and answers
    """
    progressions = [generate_progression() for _ in range(3)]
    questions = []
    answers = []

    for progression in progressions:
        question, answer = generate_question(progression)
        questions.append(question)
        answers.append(answer)

    return questions, answers


def progression_game():
    questions, answers = generate_game_data()
    play_game(questions, answers, RULES)
