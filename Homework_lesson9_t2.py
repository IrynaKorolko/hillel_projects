def difference(*args: float, int):
    """The function returns the difference between the maximum and minimum values of arguments.
    Args:
        *args: values (any number).
    Returns:
        The difference between the maximum and minimum values.
    """
    return 0 if len(args) == 0 else max(args) - min(args)