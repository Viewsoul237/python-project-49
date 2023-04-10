from random import choice
from random import randint
from brain_games.functions import greeting
from brain_games.functions import create_random_int
from brain_games.functions import give_a_task
from brain_games.functions import give_result


def calc_game():
    """Основная логика игры."""
    name = greeting()  # здороваемся и получаем имя пользователя
    print(give_a_task(1))  # печатаем задание игры
    life_counter = 3  # счетчик попыток
    for _ in range(life_counter):
        math_signs = ["+", "-", "*"]
        sign_in_game = choice(math_signs)  # генерируем случайный мат. знак
        x = create_random_int()  # генерируем случайное число
        if sign_in_game == "*":  # ограничение множителя,
            # чтобы можно было считать в уме
            y = randint(1, 15)
        else:
            y = create_random_int()  # генерируем второе случайное число

        print(f"Question: {x} {sign_in_game} {y}")
        user_answer = int(input("Your answer: "))  # получаем ответ пользователя

        match sign_in_game:  # получаем правильный ответ
            case "+":
                correct_answer = x + y
            case "-":
                correct_answer = x - y
            case _:
                correct_answer = x * y

        result = give_result(user_answer, correct_answer, name)  # сравниваем
        # ответы и печатаем соответствующий текст
        if not result:
            break
        life_counter -= 1

    if life_counter == 0:
        print(f"Congratulations, {name}!")
