def is_palindrom(text: str) -> bool:
    """Функція визначає чи є введений рядок є паліндромом
    
    Параметри: text

    Повертає: True якщо паліндром, інакше False
    """

    if text == text[::-1]:
        return True
    else:
        return False
    
    
