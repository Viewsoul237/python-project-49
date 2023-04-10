from random import randint
from brain_games.functions import greeting
from brain_games.functions import give_a_task
from brain_games.functions import give_result
from brain_games.functions import is_prime


def prime_game():
    """Основная логика игры."""
    name = greeting()  # здороваемся и получаем имя пользователя
    print(give_a_task(4))  # печатаем задание игры
    life_counter = 3  # счетчик попыток
    for _ in range(life_counter):
        temp_number = randint(1, 200)
        print(f"Question: {temp_number}")
        user_answer = input("Your answer: ")  # получаем ответ пользователя
        prime = is_prime(temp_number)
        correct_answer = "yes" if prime else "no"  # получаем корректный ответ

        result = give_result(user_answer, correct_answer, name)  # сравниваем
        # ответы и печатаем соответствующий текст
        if not result:
            break
        life_counter -= 1

    if life_counter == 0:
        print(f"Congratulations, {name}!")
