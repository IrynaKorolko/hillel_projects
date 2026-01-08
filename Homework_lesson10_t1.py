def pow(x):
    return x**2
def some_gen(begin, n, func):
    count = 0
    start_el = begin
    while count < n:
        yield start_el
        start_el = func(start_el)
        count += 1