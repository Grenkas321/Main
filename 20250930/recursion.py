def func(N, summ):
    while N > 0:
        summ += N
        N -= 1
        return func(N, summ)
    return summ
print(func(8, 0))
