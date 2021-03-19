from collections.abc import Iterable


class CustomSet:
    """Build an ordered collection of unique elements.

    Examples:
        >>> custom_set = CustomSet([1, 2, 1])
        >>> custom_set
        [1, 2]
    """

    def __init__(self, sequence):
        self.set = list()
        self.add(sequence)

    def add(self, sequence):
        """Add an element to a set."""
        if isinstance(sequence, Iterable):
            for item in sequence:
                if item not in self.set:
                    self.set.append(item)
        else:
            if sequence not in self.set:
                self.set.append(sequence)

    def clear(self):
        """Remove all elements from this set."""
        self.set = []

    def copy(self):
        """Return a shallow copy of a set."""
        return self.set.copy()

    def difference(self, *args):
        """Return the difference of two or more sets as a new set.
        (i.e. all elements that are in this set but not the others.)
        """
        list_of_difference = list()
        for other_set in args:
            for item in self.set:
                if (item not in other_set and
                        item not in list_of_difference):
                    list_of_difference.append(item)
        return CustomSet(list_of_difference)

    def difference_update(self, other_set):
        """Remove all elements of another set from this set."""
        for item in other_set:
            if item in self.set:
                self.set.remove(item)

    def discard(self, item):
        """Remove an element from a set if it is a member.
        If the element is not a member, do nothing.
        """
        if item in self.set:
            self.set.remove(item)

    def intersection(self, other_set):
        """Return the intersection of two sets as a new set.
        (i.e. all elements that are in both sets.)
        """
        list_of_same_elements = list()
        for item in other_set:
            if item in self.set:
                list_of_same_elements.append(item)
        return CustomSet(list_of_same_elements)

    def intersection_update(self, other_set):
        """Update a set with the intersection of itself and another."""
        self.set = self.intersection(other_set)

    def isdisjoint(self, other_set):
        """Return True if two sets have a null intersection."""
        return not self.intersection(other_set)

    def issubset(self, other_set):
        """Report whether another set contains this set."""
        for item in self.set:
            if item not in other_set:
                return False
        return True

    def issuperset(self, other_set):
        """Report whether this set contains another set."""
        for item in other_set:
            if item not in self.set:
                return False
        return True

    def pop(self):
        """Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        if not self.set:
            raise KeyError('Set is empty')
        return self.set.pop()

    def remove(self, item):
        """Remove an element from a set; it must be a member.
        If the element is not a member, raise a KeyError.
        """
        if item not in self.set:
            raise KeyError('Element is not a member')
        self.set.remove(item)

    def symmetric_difference(self, other_set):
        """Return the symmetric difference of two sets as a new set.
        (i.e. all elements that are in exactly one of the sets.)
        """

        result = [item for item in self.set + list(other_set)
                  if item in self.set and item not in other_set or
                  item in other_set and item not in self.set]

        return CustomSet(result)

    def symmetric_difference_update(self, other_set):
        """Update a set with the symmetric difference of itself and another."""
        self.set = self.symmetric_difference(other_set)

    def union(self, other_set):
        """Return the union of sets as a new set.
        (i.e. all elements that are in either set.)
        """
        new_set = CustomSet(other_set)
        new_set.add(self.set)
        return new_set

    def update(self, other_set):
        """Update a set with the union of itself and others."""
        self.add(other_set)

    def __and__(self, other_set):
        """Return self&value."""
        return self.intersection(other_set)

    def __contains__(self, y):
        """x.__contains__(y) <==> y in x."""
        return y in self.set

    def __eq__(self, other):
        """Return self==value."""
        return sorted(self.set) == sorted(list(other))

    def __ge__(self, other):
        """Return self>=value."""
        return self.issuperset(other)

    def __gt__(self, other):
        """Return self>value."""
        return self.__ge__(other) and self != other

    def __iand__(self, other):
        """Return self&=value."""
        self.intersection_update(other)
        return self.set

    def __ior__(self, other):
        """Return self|=value."""
        self.update(other)
        return self.set

    def __isub__(self, other):
        """Return self-=value."""
        self.difference_update(other)
        return self.set

    def __iter__(self):
        """Implement iter(self)."""
        return iter(self.set)

    def __ixor__(self, other):
        """Return self^=value."""
        self.symmetric_difference_update(other)
        return self.set

    def __len__(self):
        """Return len(self)."""
        return len(self.set)

    def __le__(self, other):
        """Return self<=value."""
        return self.issubset(other)

    def __lt__(self, other):
        """Return self<value."""
        return self.issubset(other) and self != other

    def __or__(self, other):
        """Return self|value."""
        return self.union(other)

    def __repr__(self):
        return str(self.set)

    def __sub__(self, other):
        """Return self-value."""
        return self.difference(other)

    def __xor__(self, other):
        """Return self^value."""
        return self.symmetric_difference(other)

