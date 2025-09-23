array = list()

for i in eval(input()):
    array.append([i*i % 100, i])

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i][0] > array[j][0]:
            array[i], array[j] = array[j], array[i]

answer = [i[1] for i in array]
print(answer)
