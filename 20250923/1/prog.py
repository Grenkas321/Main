a, b = eval(input())
print([i for i in range (a, b + 1) if i!=1 and all([i%j != 0 for j in range(2,i)])])
