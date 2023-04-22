from random import choice, randint


TASK_DESCRIPTION = "What is the result of the expression?"
BEGIN_RANGE = 1
END_RANGE = 100
END_RANGE_FOR_MULTIPLICATION = 15
MATH_SIGNS = ("+", "-", "*")


def calculate(num_one: int, num_two: int, sign: str) -> int:
    match sign:  # получаем правильный ответ
        case "+":
            correct_answer = num_one + num_two
        case "-":
            correct_answer = num_one - num_two
        case _:
            correct_answer = num_one * num_two
    return correct_answer


def create_question_and_answer():
    """Генерирует вопрос и ответ"""
    sign_in_game = choice(MATH_SIGNS)  # генерируем случайный мат. знак
    x = randint(BEGIN_RANGE, END_RANGE)  # генерируем случайное число
    if sign_in_game == "*":  # ограничение множителя,
        # чтобы можно было считать в уме
        y = randint(BEGIN_RANGE, END_RANGE_FOR_MULTIPLICATION)
    else:
        y = randint(BEGIN_RANGE, END_RANGE)  # генерируем второе случ. число
    question = f'{x} {sign_in_game} {y}'
    correct_answer = calculate(x, y, sign_in_game)
    return question, correct_answer
