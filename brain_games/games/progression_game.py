from random import randint
from brain_games.functions import greeting
from brain_games.functions import give_a_task
from brain_games.functions import give_result


def progression_game():
    """Основная логика игры."""
    name = greeting()  # здороваемся и получаем имя пользователя
    print(give_a_task(3))  # печатаем задание игры
    life_counter = 3  # счетчик попыток
    for _ in range(life_counter):
        progression_step = randint(2, 25)  # генерируем шаг прогрессии
        progression_start = randint(1, 20)
        progression = [str(progression_start + (progression_step * i))
                       for i in range(10)]  # создаем прогрессию с шагом

        random_position = int(randint(0, 9))
        correct_answer = int(progression[random_position])
        progression[random_position] = '..'
        print("Question:", *progression)  # выводим задание
        user_answer = int(input("Your answer: "))  # ответ пользователя
        result = give_result(user_answer, correct_answer, name)  # сравниваем
        # ответы и печатаем соответствующий текст
        if not result:  # при неудаче игра заканчивается
            break
        life_counter -= 1  # при успехе попытка вычитается

    if life_counter == 0:
        print(f"Congratulations, {name}!")
