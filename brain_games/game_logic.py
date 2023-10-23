import prompt


def play_game(questions, answers, rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    for question, correct_answer in zip(questions, answers):
        q = [x.replace(" ", "") if x == ".." else x for x in question]
        print(f"Question: {' '.join(q)}")
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer."
                f"\nCorrect answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
