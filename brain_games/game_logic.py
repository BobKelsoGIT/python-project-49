import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_game(questions, answers, description):
    name = welcome_user()  # Greet the user
    print(description)
    for question, correct_answer in zip(questions, answers):
        q = [x.replace(" ", "") if x == ".." else x for x in question]
        # print(f"Question: {q.strip('[], ')}")
        print(f"Question: {' '.join(q)}")
        user_answer = prompt.string(f'Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
