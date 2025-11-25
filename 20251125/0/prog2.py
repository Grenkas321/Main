class sole(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        if len(bases) > 1:
            raise TypeError("Cannot have more tan one parent")
        return super().__new__(mcls, name, bases, namespace, **kwargs)
