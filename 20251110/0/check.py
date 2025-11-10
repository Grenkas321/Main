def b_init(self, x): self.x = x
Base = type("Base", (), {"__init__": b_init})

def c_init(self, x):
    super(Derived, self).__init__(x + 1)
Derived = type("Derived", (Base,), {"__init__": c_init})

d = Derived(10)
print("Derived.x =", d.x)
