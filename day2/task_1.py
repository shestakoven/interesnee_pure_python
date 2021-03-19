def multiply_for(result, *args):
    """Multiply elements by for-loop.

    Args:
        result (int): init result
        *args: iterable

    Returns:
        float: result of multiplies

    """
    worked = False
    for seq in args:
        if isinstance(seq, dict):
            seq = seq.values()
        if isinstance(seq, tuple):
            raise AttributeError("'tuple' object has no attribute 'pop'")
        for elem in seq:
            try:
                elem = float(elem)
                worked = True
                result *= elem
            except ValueError as exc:
                print(exc)
    if worked:
        return result
    else:
        return 'There is no elements for composition'


def multiply_while(result, *args):
    """ multiply elements by while-loop

    Args:
        result: init result
        args: sequence of elements (set, list, dict)

    Returns:
         float: result of multiplies
    """

    i = 0
    worked = False
    while i < len(args):
        seq = args[i]
        while seq:
            if isinstance(seq, dict):
                seq = list(seq.values())
                elem = seq.pop()
            else:
                elem = seq.pop()
            try:
                elem = float(elem)
                worked = True
                result *= elem
            except ValueError as exc:
                print(exc)
        i += 1

    if worked:
        return result
    else:
        return 'There is no elements for composition'


def get_composition(*args, use_for: bool):
    """get composition from lists, sets, dicts

    Args:
        args*: sequence of elements (tuple, list, dict)
        use_for: True - use for-loop, False - use while-loop

    Returns:
        result of multiplies

    Examples:
        >>> get_composition({1, '2', 'test'},\
                            [1, '3'],\
                            {'1': 2, 2: '3'}, use_for=False)
        could not convert string to float: 'test'
        36

    """

    result = 1
    if use_for:
        result = multiply_for(result, *args)
    else:
        result = multiply_while(result, *args)

    if isinstance(result, str):
        return result

    if result % 1 == 0:  # After multiplication, the number is of float type.
        # this line checks if the number has a fractional part (after dot).
        # If not, assigns the int type to the number.
        result = int(result)

    return round(result, 2)


print(get_composition('a', use_for=True))
