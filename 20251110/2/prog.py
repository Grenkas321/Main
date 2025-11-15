import numbers

class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr: str) -> float:
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr, {"__builtins__": {}}, {})
    except Exception:
        raise InvalidInput
    coords = (x1, y1, x2, y2, x3, y3)
    if not all(isinstance(v, numbers.Real) for v in coords):
        raise BadTriangle
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    if area == 0:
        raise BadTriangle
    return area

while True:
    try:
        s = input().strip()
        a = triangleSquare(s)
    except InvalidInput:
        print("Invalid input")
        continue
    except BadTriangle:
        print("Not a triangle")
        continue
    else:
        print(f"{a:.2f}")
        break
