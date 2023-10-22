import random
from brain_games.game_logic import play_game


def generate_progression() -> [str]:
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    return [str(start + i * step) for i in range(length)]


def progression_game():

    description = 'What number is missing in the progression?'
    progression_list = []
    questions = []
    answers = []

    for _ in range(3):
        progression_list.append(generate_progression())

    for i in range(0, len(progression_list)):
        each_question_list = []
        each_question_list.extend(progression_list[i])
        index_to_replace = random.randint(0, len(each_question_list) - 1)
        correct_answer = str(each_question_list[index_to_replace])
        answers.append(correct_answer)
        for k in range(0, len(each_question_list)):
            if k == index_to_replace:
                each_question_list[k] = '..'
                questions.append(each_question_list)

    play_game(questions, answers, description)
