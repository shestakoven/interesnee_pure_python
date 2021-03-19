def fibonacci_num(n):
    if n < 1:
        raise ValueError("'n' can't be less then 1")
    if n in (1, 2):
        return 1
    return fibonacci_num(n - 1) + fibonacci_num(n - 2)
