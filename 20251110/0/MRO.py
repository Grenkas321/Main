class A: pass
class B(A): pass

try:
    Y = type("Y", (B, A), {})
    print("Y OK, MRO:", [c.__name__ for c in Y.mro()])
except TypeError as e:
    print("Y FAIL:", e)

try:
    X = type("X", (A, B), {})
    print("X OK, MRO:", [c.__name__ for c in X.mro()])
except TypeError as e:
    print("X FAIL:", e)
