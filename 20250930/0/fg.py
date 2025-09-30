def MINF(*func):
    def fun(x):
        return min([f(x) for f in func])
    return fun
