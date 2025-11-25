first_line = input().split()
if len(first_line) != 3:
    raise SystemExit("Нужно три слова")

w1, w2, w3 = first_line

while True:
    try:
        line = input()
    except EOFError:
        break

    words = line.split()
    match words:
        case [first, *rest] if first == w1 and "yes" in rest:
            print("case1")
        case [only] if only == w2:
            print("case2")
        case [first, *middle, last] if first == w3 and last == w2:
            print("case3")
        case _:
            print("no match")

