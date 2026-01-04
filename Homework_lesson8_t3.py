def find_unique_value(numbers: list) -> int:
    """
    Docstring for find_unique_value
    
    :param list: list with numbers

    :return: the unique number found
    """
    for number in numbers:
        count_d = numbers.count(d)
        if count_d == 1:
            return number