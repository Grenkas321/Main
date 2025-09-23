m1 = [eval(input())]
m2 = list()
size = len(m1[0])

for i in range(size - 1):
    m1.append(eval(input()))

for i in range(size):
    m2.append(eval(input()))

mult = []

for x in range(size):
    mult.append(list())
    for y in range(size):
        mult[x].append(0)
        for z in range(size):
            mult[x][y] += m1[x][z] * m2[z][y]

for i in range(size):
    print(','.join(str(x) for x in mult[i]))
