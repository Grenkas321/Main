def Minus(obj1,  obj2):
    if isinstance(obj1, int) or isinstance(obj1, float) or isinstance(obj1, complex):
        return obj1 - obj2
    else:
        answer = list()
        for i in obj1:
            if i not in obj2:
                answer.append(i)
        return type(obj1)(answer)

obj1, obj2 = eval(input())
print(Minus(obj1,obj2))
