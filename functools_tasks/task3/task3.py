def process_list(list_: list, order=False, filter_b=False):
    """Return processed list.

    Args:
        list_(list): Just list with elements.
        order(bool, optional): If True, function returns ordered list.
        filter_b(bool, optional): If True, function returns ordered list witt
            words, which start with `b` or `B`.

    Returns:
        Ordered list.
    """
    if filter_b:
        list_ = list(filter(lambda x: str(x)[0] in 'bB', list_))
        return sorted(list_, key=str.lower)
    if order:
        list_ = list(map(lambda x: str(x), list_))
        return sorted(list_, key=str.lower)


