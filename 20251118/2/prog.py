import sys

data = sys.stdin.buffer.read()

s = data.decode("utf-8", errors="replace")

latin_bytes = s.encode("latin1", errors="replace")
fixed = latin_bytes.decode("cp1251", errors="replace")

sys.stdout.buffer.write(fixed.encode("utf-8"))

exec(sys.stdin.read())