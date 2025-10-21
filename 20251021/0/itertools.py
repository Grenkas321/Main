from itertools import *

s = 0
print(list(islice(dropwhile(lambda x: x<=1.6, (s := s + 1/(i * i) for i in count(1))), 10)))
print(list(filterfalse(lambda x: x % 7, range(10,66))))

def repeater(seq, n):
    yield from chain.from_iterable(map(lambda x: repeat(x, n), seq))

print(list(product('ABCDEFGH', '12345678')))
