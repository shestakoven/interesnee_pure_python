
def check_items(*args, **kwargs):
    """Check arguments for all or at least one is True."""
    items_list = args + tuple(kwargs.values())
    if all(items_list):
        return 'All arguments are True'
    if not any(items_list):
        return 'All arguments are False'

    true_args = [value for value in items_list if value]
    return f'True arguments only {true_args}'
