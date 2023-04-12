from random import randint


TASK_DESCRIPTION = "Answer \"yes\" if the number is even," \
                   " otherwise answer \"no\"."
BEGIN_RANGE = 1
END_RANGE = 200


def is_even(number: int) -> bool:
    """Проверяет число на четность."""
    return number % 2 == 0


def create_question_and_answer():
    question = randint(BEGIN_RANGE, END_RANGE)
    even = is_even(question)
    correct_answer = "yes" if even else "no"  # получаем корректный ответ

    return question, correct_answer
