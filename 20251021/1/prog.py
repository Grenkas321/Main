def fib(m, n):
    prev, cur = 1, 1
    if m == 0:
        yield prev
        yield cur
    elif m == 1:
        yield cur
    for i in range(2, m+n):
        tmp = cur
        cur +=prev
        prev = tmp
        if i >=m:
            yield cur

import sys
exec(sys.stdin.read())
