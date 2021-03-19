# from itertools import chain
# print(list(chain([1, 2], (3, 4)))) #so it`s ez way(:
from collections import Iterable


def chain(*args: Iterable):
    """Concatenate together several iterables objects and returns
    iterator through all their elements (join several iterables in chains).
    """

    for item in args:
        yield from item


