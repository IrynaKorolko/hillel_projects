def pow(x) -> float:
    """The function returns the square of x

    Parameters: A number to be squared.

    Returns: The square of x.
    """
    return x ** 2


def some_gen(begin, n, func) -> object:
    """The generator yields n elements, starting from 
    begin to get the next element.

    Parameters:
        begin: The starting element.
        n: The number of elements.
        func: A function that takes one argument and returns the next element.

    Yields:
        The next element in the sequence.
    """
    count = 0
    start_el = begin
    while count < n:
        yield start_el
        start_el = func(start_el)
        count += 1
