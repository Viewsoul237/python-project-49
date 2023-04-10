import prompt
from random import randint


def create_random_int():
    """Возвращает случайное число от 1 до 100 включительно."""
    begin = 1
    end = 100
    random_number = randint(begin, end)
    return random_number


def is_even(number: int) -> bool:
    """Проверяет число на четность."""
    return number % 2 == 0


def greeting() -> str:
    """Здоровается и возвращает имя пользователя."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ').capitalize()
    print(f"Hello, {name}!")
    return name


def give_a_task(number_of_game):
    """Печатает задание к выбранной игре.

    even - игра номер 0
    calc - игра номер 1
    gcd - игра номер 2
    progression - игра номер 3
    prime - игра номер 4
    """
    tasks = ["Answer \"yes\" if the number is even, otherwise answer \"no\".",
             "What is the result of the expression?",
             "Find the greatest common divisor of given numbers.",
             "What number is missing in the progression?",
             'Answer "yes" if given number is prime. Otherwise answer "no".']
    return tasks[number_of_game]


def give_result(user_answer, correct_answer, user_name) -> bool:
    """Сравнивает ответ пользователя с корректным, печатает вывод."""
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
        return False


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


def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, number + 1 // 2):
        if number % i == 0:
            return False
    return True
