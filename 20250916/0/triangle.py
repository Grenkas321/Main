a, b, c = eval(input())
if ((a + b + c) - max(a,b,c) > max(a, b, c)):
    print('True')
else:
    print('False')
