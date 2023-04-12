from random import randint


TASK_DESCRIPTION = "Find the greatest common divisor of given numbers."
BEGIN_RANGE = 1
END_RANGE = 100


def find_gcd(first_num, second_num):
    """Возвращает наибольший общий делитель двух чисел (НОД)"""
    dividers = []
    for i in range(1, first_num + 1):
        # заполняем список dividers делителями first_num
        if first_num % i == 0:
            dividers.append(i)
    dividers.reverse()
    for elem in dividers:
        if second_num % elem == 0:
            return elem


def create_question_and_answer():
    first_number = randint(BEGIN_RANGE, END_RANGE)
    second_number = randint(BEGIN_RANGE, END_RANGE)
    question = f'{first_number} {second_number}'
    correct_answer = find_gcd(first_number, second_number)  # вычисляем НОД

    return question, correct_answer
