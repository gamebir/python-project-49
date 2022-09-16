import prompt
MAX_COUNT = 3


def greeting():
    """greeting"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}')
    return name


def game_engine(question, rite_answer, name):
    """game engine"""
    max_count = MAX_COUNT
    count = 0
    while count < max_count:
        print(f'Question: {question[count]}')
        answer = prompt.string('Your answer: ')
        if rite_answer[count] == answer:
            print('Correct')
            count += 1
        else:
            print(
                f"'{answer}'is wrong answer ;(. Correct answer was "
                f"'{rite_answer[count]}'.\nLet's try again, {name}!"
            )
            break
    if count == MAX_COUNT:
        print(f'Congratulations, {name}!')
