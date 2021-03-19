from itertools import islice


class Yrange:
    """Unlimited iterator from 1 to desire number.

    Args:
        last_num(int): The last number of the sequence.

    Examples:
        >>> for num in islice(Yrange(3), 4):
        >>>    print(num)
        1, 2, 3, 1

    """

    def __init__(self, last_num):
        self.last_num = last_num
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.last_num:
            self.counter += 1
            return self.counter
        self.counter = 1
        return self.counter


def yrange(last_num):
    """Unlimited generator from 1 to desire number.

    Args:
        last_num(int): The last number of the sequence.

    Examples:
        for num in islice(yrange(3), 4):
            print(num)
        1, 2, 3, 1

    """
    counter = 0
    while True:
        if counter < last_num:
            counter += 1
            yield counter
        else:
            counter = 1
            yield counter
