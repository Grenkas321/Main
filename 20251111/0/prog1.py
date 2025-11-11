def decor(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@decor
def fun(a,b):
    return a*2+b

@decor
def isint(*args):
    for i in args:
        if type(i) != type(1):
            raise TypeError
    return True
