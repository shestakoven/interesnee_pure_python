class ReverseIter:
    """Iterate reversed sequence.

    Examples:
        for i in ReverseIter([1, 2, 3]):
            print(i)
        3
        2
        1
        
    """
    def __init__(self, seq):
        self.seq = seq

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > len(self.seq):
            raise StopIteration
        return self.seq[-self.i]


