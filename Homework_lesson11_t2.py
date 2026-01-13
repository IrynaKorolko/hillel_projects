def generate_cube_numbers(end) -> int:
    """Generate a list of cube numbers from 1 to end (set by user).

    Parameters:
        end(int): The upper limit

    Return:
        list: A list of cube numbers from 1 to end.
    """
    el = 2
    number_in_cube = el ** 3
    while number_in_cube < end:
        yield number_in_cube
        el += 1
        number_in_cube = el ** 3