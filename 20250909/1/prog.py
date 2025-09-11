a, b, c = eval(input())

if (a > c):
    (c, a) = (a, c)
if (b > c):
    (b, c) = (c, b)
if (a > b):
    (a, b) = (b,a)

print(a, b, c, sep = ", ")
