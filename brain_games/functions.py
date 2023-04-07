import prompt
from random import randint


def create_random_int():
    """Возвращает случайное число от 1 до 100 включительно."""
    begin = 1
    end = 100
    random_number = randint(begin, end)
    return random_number


def is_even(number):
    """ Проверяет число на четность"""
    return number % 2 == 0


def game():
    """Основная логика игры."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ').capitalize()
    print(f"Hello, {name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    life_counter = 3
    for _ in range(life_counter):
        temp_number = create_random_int()
        print(f"Question: {temp_number}")
        user_answer = input("Your answer: ")
        even = is_even(temp_number)

        if (even and user_answer == "yes") or\
                (not even and user_answer == "no"):
            print("Correct!")
            life_counter -= 1
        else:
            if not even:
                print(f"'{user_answer}' is wrong answer ;(."
                      f" Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
            else:
                print(f"'{user_answer}' is wrong answer ;(."
                      f" Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
    if life_counter == 0:
        print(f"Congratulations, {name}!")
