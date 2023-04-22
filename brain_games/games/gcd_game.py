from random import randint


TASK_DESCRIPTION = "Find the greatest common divisor of given numbers."
BEGIN_RANGE = 1
END_RANGE = 100


def find_gcd(first_num: int, second_num: int) -> int:
    """Возвращает наибольший общий делитель двух чисел (НОД)"""
    while second_num != 0:
        first_num, second_num = second_num, first_num % second_num
    return first_num


def create_question_and_answer():
    first_number = randint(BEGIN_RANGE, END_RANGE)
    second_number = randint(BEGIN_RANGE, END_RANGE)
    question = f'{first_number} {second_number}'
    correct_answer = find_gcd(first_number, second_number)  # вычисляем НОД

    return question, correct_answer
