from itertools import islice, tee

def slide(seq, n):
    yield from (i for st in range(len(seq)) for i in islice(seq, st, st + n))

import sys
exec(sys.stdin.read())
