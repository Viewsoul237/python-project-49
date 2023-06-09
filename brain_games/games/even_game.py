from random import randint

from brain_games.utils import set_response_type

TASK_DESCRIPTION = "Answer \"yes\" if the number is even," \
                   " otherwise answer \"no\"."
BEGIN_RANGE = 1
END_RANGE = 200


def is_even(number: int) -> bool:
    """Проверяет число на четность."""
    return number % 2 == 0


def create_question_and_answer():
    question = randint(BEGIN_RANGE, END_RANGE)
    correct_answer = set_response_type(is_even(question))
    return question, correct_answer
