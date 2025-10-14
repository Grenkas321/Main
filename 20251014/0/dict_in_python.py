s = input()
a, b = eval(input())
x = a
y = b
print(eval(s))
x, y = y, x
print(eval(s))
