matrix = []
while c := input():
    c = eval(c)
    matrix.append(c)
if any([len(line)!= len(matrix) for line in matrix]):
    print("Non-square")
    exit()
    

for j in range(len(matrix)):
    for v in range (j+1, len(matrix)):
        matrix[j][v], matrix[v][j] = matrix[v][j], matrix[j][v]

for line in matrix:
    print(*line)
