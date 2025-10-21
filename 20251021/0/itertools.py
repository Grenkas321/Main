from itertools import *

s = 0
print(list(islice(dropwhile(lambda x: x<=1.6, (s := s + 1/(i * i) for i in count(1))), 10)))
n = int(input())
print(list(filterfalse(lambda x: x % n, range(10,66))))

def repeater(seq, n):
    yield from chain.from_iterable(map(lambda x: repeat(x, n), seq))

print(list(starmap(str.__add__, product('ABCDEFGH', '12345678'))))
