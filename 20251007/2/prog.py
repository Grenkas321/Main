from math import *
W, H, A, B, f = input().split()
W, H, A, B = int(W), int(H), int(A), int(B), 
screen = [[' '] * W for i in range(H)]


def scale(a, b, A, B, x):
    return (B - A) * (x - a)/(b - a) + A


def show(screen):
    print('\n'.join(["".join(s) for s in screen]))


min_y = min([eval(f) for x in range(A, B + 1)])
max_y = max([eval(f) for x in range(A, B + 1)])
last_y = H + 1
last_x = W + 1
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = eval(f)
    shift = round(scale(min_y, max_y, 0, H - 1, y))
    if last_y > H:
        last_x = i
        last_y = H - shift - 1
    else:
        #make a line
        if sqrt((i - last_x)**2 + (H - shift - 1 - last_y)**2) > 1:
            for j in range(min(H - shift - 1, last_y) +1 , max(H - shift - 1, last_y)):
                screen[j][i] = '*'
        last_x = i
        last_y = H - shift - 1
    screen[H - shift - 1][i] = '*'
show(screen)
