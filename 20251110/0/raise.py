def div(a, b, eps=1e-9):
    if abs(b) < eps:
        raise ZeroDivisionError("denominator ~ 0")
    return a / b

print("div(4,2) =", div(4,2))
try:
    print(div(1, 1e-12, eps=1e-6))
except ZeroDivisionError as e:
    print("Поймано:", e)
