ERROR_MSG = 'Invalid value. Input number from 1 to 8'
WIN_MSG = 'The cube was assembled'
CUBE_SET = {1, 2, 3, 4, 5, 6}


def check_number(num):
    try:
        num = int(num)
    except ValueError:
        print(ERROR_MSG)
        return False
    if num < 1 or num > 8:
        print(ERROR_MSG)
        return False
    if num not in CUBE_SET:
        return False
    return True


def wait_for_cube():
    """Wait for 1-2-3-4-5-6 from input.

    Returns:
        WIN_MSG (str): Congratulations.

    """

    user_set = set()

    while True:
        num = input()
        if not check_number(num):
            continue
        user_set.add(int(num))
        if CUBE_SET == user_set:
            return WIN_MSG
