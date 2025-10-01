def Pareto(*pairs):
    answer = tuple()
    for i in pairs:
        for j in pairs:
            if i!=j and (i[0] <= j[0] and i[1] <= j[1]) and (i[0] < j[0] or i[1] < j[1]):
                break
        else:
            answer += ((i), )

    return answer

print(Pareto(*eval(input())))
