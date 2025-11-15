class Num:
    def __init__(self):
        self._slot = None

    def __set_name__(self, owner, name):
        self._slot = f"__num_slot_{name}_{id(self)}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return instance.__dict__.get(self._slot, 0)

    def __set__(self, instance, value):
        if hasattr(value, "real"):
            v = value.real
        elif hasattr(value, "__len__"):
            v = len(value)
        else:
            v = value
        instance.__dict__[self._slot] = v

import sys
exec(sys.stdin.read())