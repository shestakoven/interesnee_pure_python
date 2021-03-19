def move(number, times_count):
    """Cyclically shifts the last 3 characters of number.

        If times_count > 0, shift to the right,
        else shift to the left.

    Args:
        number (int, str): Number in which to perform the shift.
        times_count (int, str): Times of shifts.

    Returns:
        int: Number with shifts

    """
    if not isinstance(number, int):
        return 'Number must be integer'
    number = str(number)
    last_digits = list(number[-3:])
    if times_count < 0:
        times_count = abs(times_count)
        for i in range(times_count):
            last_digits.append(last_digits.pop(0))
    else:
        last_digits.insert(0, last_digits.pop())
    last_digits = ''.join(last_digits)
    return int(number[:-3] + last_digits)
