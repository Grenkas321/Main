from itertools import count

def gen():
    s = 0
    for i in count(1):
        s += 1/(i*i)
        yield s

g = sum(1/(i*i) for i in range(1, 10000))

print(gen)
print(g)
