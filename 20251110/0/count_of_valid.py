class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

cands = [
    (C, A), (A, C),
    (C, B), (B, C),
    (C, D), (D, C),
]

ok = 0
for p, q in cands:
    try:
        E = type("E", (p, q), {})
        ok += 1
        print(f"E({p.__name__}, {q.__name__}) OK, MRO:", [c.__name__ for c in E.mro()])
    except TypeError as e:
        print(f"E({p.__name__}, {q.__name__}) FAIL:", e)

print("Итого валидных вариантов:", ok, "из", len(cands))
