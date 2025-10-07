from decimal import Decimal, getcontext
getcontext().prec = 100

def esum(N, one):
    e, f = one, one
    for n in range (1, N+1):
        f*=n
        e+= one/f
    return e

print(esum(10,Decimal("1")))


