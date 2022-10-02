import prompt
MAX_ATTEMPTS = 3


def engine_play(game, TASK):
    """game engine"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}')
    print(TASK)
    atempt = 0
    while atempt < MAX_ATTEMPTS:
        question, correct_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct !')
            atempt += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {name}!"
            )
            break
    if atempt == MAX_ATTEMPTS:
        print(f'Congratulations, {name}!')
