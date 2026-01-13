def is_even(number) -> bool:
    """The function is to check if a number is even.

    Parameters:
        number(int): The number we check

    Return:
        bool: True if the number is even, False otherwise.
    """
    return number & 1 == 0
