class Vowel:
    __slots__ = ("a", "e", "i", "o", "u", "y")

    def __init__(self, **kwargs):
        for k in kwargs:
            if k not in self.__slots__:
                raise TypeError(f"unknown slot: {k}")
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def answer(self):
        return 42

    @answer.setter
    def answer(self, _):
        raise AttributeError("answer is read-only")

    @property
    def full(self):
        return all(hasattr(self, name) for name in self.__slots__)

    @full.setter
    def full(self, _):
        pass

    def __str__(self):
        parts = []
        for name in sorted(self.__slots__):
            if hasattr(self, name):
                parts.append(f"{name}: {getattr(self, name)}")
        return ", ".join(parts)


import sys
exec(sys.stdin.read())