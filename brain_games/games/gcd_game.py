from brain_games.functions import greeting
from brain_games.functions import give_a_task
from brain_games.functions import create_random_int
from brain_games.functions import find_gcd
from brain_games.functions import give_result


def gcd_game():
    """Основная логика игры."""
    name = greeting()  # здороваемся и получаем имя пользователя
    print(give_a_task(2))
    life_counter = 3  # счетчик попыток
    for _ in range(life_counter):
        first_number = create_random_int()
        second_number = create_random_int()
        print(f"Question: {first_number} {second_number}")
        user_answer = int(input("Your answer: "))  # ответ пользователя
        correct_answer = find_gcd(first_number, second_number)  # вычисляем НОД
        result = give_result(user_answer, correct_answer, name)  # сравниваем
        #  ответы и печатаем соответствующий текст
        if not result:
            break
        life_counter -= 1

    if life_counter == 0:
        print(f"Congratulations, {name}!")
