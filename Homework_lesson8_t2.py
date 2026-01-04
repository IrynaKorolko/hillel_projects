def is_palindrom(text: str) -> bool:
    """Функція визначає чи є введений рядок є паліндромом
    
    Параметри: text

    Повертає: True якщо паліндром, інакше False
    """

    return True if text == text[::-1] else False