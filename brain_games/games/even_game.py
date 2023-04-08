from brain_games.functions import greeting
from brain_games.functions import create_random_int
from brain_games.functions import give_a_task
from brain_games.functions import is_even
from brain_games.functions import give_result


def even_game():
    """Основная логика игры."""
    name = greeting()  # здороваемся и получаем имя пользователя
    print(give_a_task(0))  # печатаем задание игры
    life_counter = 3  # наши жизни
    for _ in range(life_counter):
        temp_number = create_random_int()  # генерируем случайное число
        print(f"Question: {temp_number}")
        user_answer = input("Your answer: ")  # получаем ответ пользователя
        even = is_even(temp_number)
        correct_answer = "yes" if even else "no"  # получаем корректный ответ

        result = give_result(user_answer, correct_answer, name)  # сравниваем
        # ответы и печатаем соответствующий текст
        if not result:
            break
        life_counter -= 1

    if life_counter == 0:
        print(f"Congratulations, {name}!")
