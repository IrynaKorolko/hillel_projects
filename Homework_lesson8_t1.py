def add_one(some_list:list) -> list:
    """Функція приймає список з цифр, які складають число, яке потрібно збільшити на один  і повернути типу list. 
    Аргументи:
    some_list - список цифр, що представляють число
    Повертає:
    list - число збільшене на один у вигляді списку"""
    
    some_list_str = ''.join(str(d) for d in some_list)
    some_list_int = int(some_list_str) + 1
    return [int(d) for d in str(some_list_int)]