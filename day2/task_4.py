ERRORS_MSGS = {
    'invalid_type':
        'Invalid data. Type of data must be list of dicts'
}


def make_list_of_same_dicts(result_dict):
    """Create list of dicts

    Args:
        result_dict (dict): Dict with all key_value: count.

    Returns:
        new_list (list): List of dicts without count == 1

    """

    new_list = []
    for key, value in result_dict.items():
        if value > 1:
            dict_ = {'key': key[0], 'value': key[1], 'count': value}
            new_list.append(dict_)
    return new_list


def validate(data):
    """Validate income parameter.

        Data must be list or tuple with dicts inside.

    Args:
        data (list): List of dicts.

    Returns:
        bool: False if data not list or tuple and
            elements of data not dicts.
    """
    if type(data) not in (list, tuple):
        return False
    for dict_ in data:
        if not isinstance(dict_, dict):
            return False
    return True


def calculate(list_of_dicts):
    """Calculate count of same values of dicts.

    Args:
        list_of_dicts (list): List of dicts.

    Returns:
        list_of_results (list): List of dicts with
            key, value and number of duplicates

    """

    if not validate(list_of_dicts):
        return ERRORS_MSGS['invalid_type']

    result_dict = dict()
    for dict_ in list_of_dicts:
        for item in dict_.items():
            if item in result_dict:
                result_dict[item] += 1
            else:
                result_dict[item] = 1
    list_of_results = make_list_of_same_dicts(result_dict)
    return list_of_results


list_dict = [
    {
        'id': 1,
        'success': True,
        'name': 'Larry',
    },
    {
        'id': 2,
        'success': False,
        'name': 'Rabi',
    },
    {
        'id': 3,
        'success': True,
        'name': 'Alex',
    }
]
