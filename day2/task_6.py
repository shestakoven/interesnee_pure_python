def get_different_keys(*args):
    """Get list with unique keys from list of dicts.

    Args:
        *args: Iterable.

    Returns:
        List of unique keys.

    """
    keys = set()
    for _dict in args:
        if not isinstance(_dict, dict):
            return f'{_dict} is not dict'
        keys ^= (set(_dict.keys()))
    return list(keys)
