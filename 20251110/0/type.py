FIELD = "Q-Q!"

def base_init(self, value):
    setattr(self, FIELD, value)

def base_str(self):
    return f"[{getattr(self, FIELD)}]"

BaseDyn = type("BaseDyn", (), {FIELD: None, "__init__": base_init, "__str__": base_str})

def child_init(self, value):
    super(DerivedDyn, self).__init__(value + 1)

DerivedDyn = type("DerivedDyn", (BaseDyn,), {"__init__": child_init})

x = BaseDyn(7)
y = DerivedDyn(7)
print("BaseDyn:", str(x), "->", getattr(x, FIELD))
print("DerivedDyn:", str(y), "->", getattr(y, FIELD))
