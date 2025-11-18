import sys

with open('file', 'br+') as file:
    center = file.seek(0, 2) // 2
    file.seek(0, 0)
    first = file.read(center)
    second = file.read(center)
    file.seek(0, 0)
    file.write(second)
    file.write(first)

