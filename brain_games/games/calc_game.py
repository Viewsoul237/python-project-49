from random import randint
from random import choice


TASK_DESCRIPTION = "What is the result of the expression?"
BEGIN_RANGE = 1
END_RANGE = 100
END_RANGE_FOR_MULTIPLICATION = 15


def create_question_and_answer():
    """Генерирует вопрос и ответ"""
    math_signs = ["+", "-", "*"]
    sign_in_game = choice(math_signs)  # генерируем случайный мат. знак
    x = randint(BEGIN_RANGE, END_RANGE)  # генерируем случайное число
    if sign_in_game == "*":  # ограничение множителя,
        # чтобы можно было считать в уме
        y = randint(BEGIN_RANGE, END_RANGE_FOR_MULTIPLICATION)
    else:
        y = randint(BEGIN_RANGE, END_RANGE)  # генерируем второе случ. число
    question = f'{x} {sign_in_game} {y}'

    match sign_in_game:  # получаем правильный ответ
        case "+":
            correct_answer = x + y
        case "-":
            correct_answer = x - y
        case _:
            correct_answer = x * y

    return question, correct_answer
