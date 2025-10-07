
from math import sin
W,H = eval(input())
A,B = eval(input())
screen = [['.'] *W for i in range(H)]
sc = "\n".join("".join(line) for line in screen)

def scale(a,b, A, B, x):
    return (x - a)*(B-A)/(b-a) + A

for line in range(0, H):
    x = scale(0, H-1, A, B, line)
    y = sin(x)
    k = round(scale(-1,1,0,W-1,y)) 
    sc[line][k+1] = "#"
