from functools import partial
from itertools import product


def get_combinations(list_: list, combination_length: int):
    """Return list of combinations with desired length from list`s elements."""
    combinations = product(list_, repeat=combination_length)
    return list(combinations)


get_comb_len_2 = partial(get_combinations, combination_length=2)
