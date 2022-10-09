from random import randint


BEGIN_RANGE = 0
END_RANGE = 100
BEGIN_STEP = 3
END_STEP = 10
BEGIN_LENGHT = 10
END_LENGHT = 20
TASK = "What number is missing in the progression?"


def generate_progression(step_progr, lenght_progr):
    """generating a sequence"""
    result = []
    n = randint(BEGIN_RANGE, END_RANGE)
    for i in range(n, n + (step_progr * lenght_progr), step_progr):
        result.append(str(i))
    return result


def get_question_correct_answer():
    progression = generate_progression(
        randint(BEGIN_STEP, END_STEP), randint(BEGIN_LENGHT, END_LENGHT)
    )
    index_replase = randint(BEGIN_RANGE, len(progression) - 1)
    correct_answer = progression[index_replase]
    progression[index_replase] = '..'
    question = ' '.join(progression)
    return question, correct_answer
