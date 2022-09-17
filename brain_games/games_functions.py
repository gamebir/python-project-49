import prompt
MAX_COUNT = 3


def greeting():
    """greeting"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}')
    return name


def game_engine(funk, max_count=MAX_COUNT):
    """game engine"""
    name = greeting()
    _, _, task = funk()
    print(task)
    count = 0
    while count < max_count:
        question, rite_answer, _ = funk()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if rite_answer == answer:
            print('Correct')
            count += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{rite_answer}'.\nLet's try again, {name}!"
            )
            break
    if count == MAX_COUNT:
        print(f'Congratulations, {name}!')
