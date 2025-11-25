class Checked:
    a: int

    def __init__(self, val):
        expected = type(self).__annotations__["a"]
        if not isinstance(val, expected):
            raise TypeError(f"expected {expected}, got {type(val)}")
        self.a = val
