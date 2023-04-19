from random import randint

from brain_games.engine import set_response_type

TASK_DESCRIPTION = 'Answer "yes" if given number is prime. ' \
                   'Otherwise answer "no".'
BEGIN_RANGE = 1
END_RANGE = 200


def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def create_question_and_answer():
    """Генерирует вопрос и ответ"""
    question = randint(BEGIN_RANGE, END_RANGE)
    correct_answer = set_response_type(is_prime(question))

    return question, correct_answer
