def prime_generator(end):
    """Generate prime numbers up to a limit set.

    Args:
        end (int): The upper limit.

    Yields:
        int: The next prime number in the list.
    """
    for num in range(2, end + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            


