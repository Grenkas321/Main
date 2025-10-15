from math import *

def inter(f_args, args):
    ind = 0
    func = f_args[-1]
    for i in f_args[:-1]:
        func = func.replace(i,args[ind])
        ind += 1
    print(eval(func))

fun = {"quit": ["cnt_f", "cnt_s", "x", "x.format(cnt_f, cnt_s)"]}
cnt = 0
while True:
    s = input()
    cnt += 1
    if s[0] == ':':
        s = s.split()
        fun[s[0][1:]] = s[1:]
    else:
        s_copy = s.split()
        if s_copy[0] == 'quit':
            arg = s.split(maxsplit=1)[1]
            inter(fun[s_copy[0]], [str(len(fun.keys())), str(cnt), arg])
            break
        if len(fun[s_copy[0]]) == 2:
            arg = s.split(maxsplit=1)[1]
            inter(fun[s_copy[0]], [arg])
        else:
            inter(fun[s_copy[0]], s_copy[1:])
