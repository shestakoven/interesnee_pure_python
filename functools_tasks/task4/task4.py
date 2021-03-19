from itertools import product


def get_combinations(list_: list, combination_length=2):
    """Return list of combinations with desired length from list`s elements."""
    combinations = product(list_, repeat=combination_length)
    return list(combinations)
