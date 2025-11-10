class A: pass
A.v = 1

class B(A): pass
B.v = 2

b = B()
b.v = 3

print("b.v (as object):", b.v)

del b.v
print("b.v (after del b.v):", b.v)

delattr(B, "v")
print("b.v (after del B.v):", b.v)
