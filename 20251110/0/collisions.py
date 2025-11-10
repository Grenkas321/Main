class Base:
    def __init__(self):
        self.__hidden = "base"

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__hidden = "child"

obj = Child()
print(hasattr(obj, "_Base__hidden"), hasattr(obj, "_Child__hidden"))
