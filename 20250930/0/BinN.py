def BinN(n, ones, base = 0):
    if n == 0 and ones == 0:
        print(base)
        return
    elif n != 0 and ones != 0:
        BinN(n-1, ones-1, base*2+1)
    if n != 0:
        BinN(n-1, ones, base*2)

BinN(*eval(input()))
        

