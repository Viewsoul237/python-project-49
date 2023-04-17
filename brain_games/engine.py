import prompt

LIFE_COUNTER = 3
CORRECT_ANSWER = "yes"
INCORRECT_ANSWER = "no"


def set_yes_or_no(answer: bool) -> str:
    """Возвращает строку 'yes' или 'no' в зависимости от аргумента"""
    if answer:
        return CORRECT_ANSWER
    return INCORRECT_ANSWER


def greeting() -> str:
    """Здоровается и возвращает имя пользователя."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ').capitalize()
    print(f"Hello, {name}!")
    return name


def give_result(user_answer, correct_answer, user_name) -> bool:
    """Сравнивает ответ пользователя с корректным, печатает вывод."""
    if user_answer.lower() == str(correct_answer):
        print("Correct!")
        return True
    print(f"'{user_answer}' is wrong answer ;(."
          f" Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")
    return False


def run_game(task, question_and_answer):
    """Движок игры"""
    name = greeting()  # печатаем задание игры
    print(task)
    for _ in range(LIFE_COUNTER):
        temp_question, correct_answer = question_and_answer()  # создаем
        # вопрос и ответ
        print(f"Question: {temp_question}")  # печатаем вопрос
        user_answer = input("Your answer: ")  # получаем ответ пользователя
        result = give_result(user_answer, correct_answer, name)  # сравниваем
        # ответы и печатаем соответствующий текст
        if not result:
            return  # выход из игры, при неправильном ответе
    print(f"Congratulations, {name}!")
