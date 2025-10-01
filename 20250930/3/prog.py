from math import *

def Calc(s, t, u):
    def func(x):
        def f_s(x):
            return eval(s)
        def f_t(x):
            return eval(t)
        def f_u(x,y):
            return eval(u)
        return f_u(f_s(x),f_t(x))
    return func

s, t, u = eval(input())
x = eval(input())
print(Calc(s, t, u)(x))
