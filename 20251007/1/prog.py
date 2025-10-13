from fractions import Fraction as Frac

def check (s, w, deg_A, cf_A, deg_B, cf_B):
    s = Frac(s)
    w = Frac(w)
    cf_A = [Frac(i) for i in cf_A]
    cf_B = [Frac(i) for i in cf_B]

    A = Frac(0)
    for i, cf in enumerate(cf_A):
        A += cf * (s ** (deg_A - i))

    B = Frac(0)
    for i, cf in enumerate(cf_B):
        B += cf * (s ** (deg_B - i))

    if B == 0:
        return False
    return A/B == w


inn = input().split(', ')
print(check(inn[0], inn[1], int(inn[2]), inn[3:3+int(inn[2])+1], int(inn[3+int(inn[2])+1]), inn[3+int(inn[2])+2:]))
