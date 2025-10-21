from itertools import count

def gen(n):
    s = 0
    for i in count(n+1):
        s += 1/(i*i)
        yield s

g = sum(1/(i*i) for i in range(1, 10000))

n = int(input())
print(gen(n))
print(g)
