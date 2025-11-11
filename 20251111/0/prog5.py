class Counter:
    def __init__(self):
        self.value = 0

    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return self.value

    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        self.value = val

class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1
c = C()
print(c.counter)
d = C()
print(d.counter)
del c
print(d.counter)