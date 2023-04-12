from random import randint


TASK_DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_STEP_RANGE_BEGIN = 2
PROGRESSION_STEP_RANGE_END = 25
PROGRESSION_START_RANGE_BEGIN = 1
PROGRESSION_START_RANGE_END = 20
RANDOM_POSITION_RANGE_BEGIN = 0
RANDOM_POSITION_RANGE_END = 9


def create_question_and_answer():
    progression_step = randint(PROGRESSION_STEP_RANGE_BEGIN,
                               PROGRESSION_STEP_RANGE_END)
    # генерируем шаг прогрессии
    progression_start = randint(PROGRESSION_START_RANGE_BEGIN,
                                RANDOM_POSITION_RANGE_END)

    progression = [str(progression_start + (progression_step * i))
                   for i in range(10)]  # создаем прогрессию с шагом
    random_position = int(randint(RANDOM_POSITION_RANGE_BEGIN,
                                  RANDOM_POSITION_RANGE_END))
    correct_answer = int(progression[random_position])
    progression[random_position] = '..'
    question = " ".join(progression).strip()

    return question, correct_answer
