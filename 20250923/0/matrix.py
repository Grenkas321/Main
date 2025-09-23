matrix = []
i = 0
while c := input():
    c = eval(c)
    matrix.append(c)
    i += 1

for j in range(len(matrix)):
    for v in range (j+1, len(matrix)):
        matrix[j][v], matrix[v][j] = matrix[v][j], matrix[j][v]

for line in matrix:
    print(*line)
