class Obj:
    pass


def update_object(obj, **kwargs):
    """Update object attributes."""
    for key, value in kwargs.items():
        if not hasattr(obj, key):
            setattr(obj, key, value)
    return obj


if __name__ == '__main__':
    obj = Obj()
    print(vars(update_object(obj, x=1, b='x')))
