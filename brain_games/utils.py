POSITIVE_ANSWER = "yes"
NEGATIVE_ANSWER = "no"


def set_response_type(answer: bool) -> str:
    """Возвращает тип ответа (положительный или отрицательный)"""
    if answer:
        return POSITIVE_ANSWER
    return NEGATIVE_ANSWER
