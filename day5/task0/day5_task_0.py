class BaseDict:
    """Default class of all dicts.

    Pass the dictionary as a parameter to create an instance
    for each class.

    Examples:
    d = ClassName({'foo': {'bar': {'foobar: 42'}})

    """

    def initial(self, class_, protected=None):
        dict_ = self.dict_
        for key, value in dict_.items():
            if isinstance(value, dict):
                if protected:
                    value = class_(value, protected)
                else:
                    value = class_(value)
            dict_[key] = value

    def __getattr__(self, item):
        return self.dict_[item]

    def __delattr__(self, item):
        raise PermissionError('You can`t delete anything')

    def __repr__(self):
        return str(self.dict_)


class ReadOnlyDict(BaseDict):
    """DotMap which you can only read."""

    def __init__(self, dict_):
        super().__setattr__('dict_', dict_)
        self.initial(ReadOnlyDict)

    def __setattr__(self, key, value):
        raise PermissionError('Read only')


class ReadAndModifyDict(BaseDict):
    """DotMap which you can only read and modify."""

    def __init__(self, dict_):
        super().__setattr__('dict_', dict_)
        self.initial(ReadAndModifyDict)

    def __setattr__(self, key, value):
        try:
            if self.__getattr__(key):
                self.dict_[key] = value
        except KeyError:
            raise PermissionError('You can`t add new key')


class RMDDict(BaseDict):
    """DotMap which you can read, modify and delete items."""

    def __init__(self, dict_):
        super().__setattr__('dict_', dict_)
        self.initial(RMDDict)

    def __setattr__(self, key, value):
        try:
            if self.__getattr__(key):
                self.dict_[key] = value
        except KeyError:
            raise PermissionError('You still can`t add new key.')

    def __delattr__(self, item):
        del self.dict_[item]


class DotMap(BaseDict):
    """Regular DotMap dict."""

    def __init__(self, dict_):
        super().__setattr__('dict_', dict_)
        self.initial(DotMap)

    def __setattr__(self, key, value):
        self.dict_[key] = value

    def __delattr__(self, item):
        del self.dict_[item]


class ProtectKeysDotMap(BaseDict):
    """Regular DotMap, where you can protect keys."""

    def __init__(self, dict_, protected):
        super().__setattr__('dict_', dict_)
        super().__setattr__('protected', protected)
        self.initial(ProtectKeysDotMap, protected=protected)

    def __getattr__(self, item):
        if item in self.protected:
            raise PermissionError('These keys are protected')
        return super().__getattr__(item)

    def __setattr__(self, key, value):
        if key in self.protected:
            raise PermissionError('These keys are protected')
        self.dict_[key] = value
