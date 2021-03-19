def merge_dicts(*args):
    """ Merge dicts into one from two or more.

        If there are duplicate keys in dictionaries, the last key will be added.

    Args:
        *args: Iterable.

    Returns:
        new_dict: Merged dict.
    """
    new_dict = dict()
    for _dict in args:
        if not isinstance(_dict, dict):
            return f'{_dict} is not dict'
        new_dict_keys = new_dict.keys()
        for key, value in _dict.items():
            if key in new_dict_keys:
                print(f'WARNING! There is duplicate "{key}" key')
            new_dict[key] = value
    return new_dict
