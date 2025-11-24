import sys

data = sys.stdin.buffer.read()

# Убираем возможные перевод(ы) строки в конце (CMD / тесты часто их добавляют)
while data and data[-1] in (10, 13):  # \n, \r
    data = data[:-1]

if not data:
    sys.exit(0)

N = data[0]
tail = data[1:]

if N <= 0:
    sys.stdout.buffer.write(data)
    sys.exit(0)

L = len(tail)

bounds = [int(L * i / N) for i in range(N + 1)]
parts = [tail[bounds[i]:bounds[i + 1]] for i in range(N)]

sorted_tail = b"".join(sorted(parts))

sys.stdout.buffer.write(data[:1] + sorted_tail)
