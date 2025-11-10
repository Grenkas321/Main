class Problem:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.__class__(self.x + other.x)
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x})"

class Problem_2(Problem): pass


a, b = Problem_2(10), Problem_2(5)
c = a + b
print(c, type(c).__name__)
