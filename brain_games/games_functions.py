import prompt
MAX_ATTEMPTS = 3


def game_engine(funk):
    """game engine"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}')
    _, _, task = funk()
    print(task)
    max_attempts=MAX_ATTEMPTS
    atempt = 0
    while atempt < max_attempts:
        question, correct_answer, _ = funk()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct')
            atempt += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {name}!"
            )
            break
    if atempt == max_attempts:
        print(f'Congratulations, {name}!')
