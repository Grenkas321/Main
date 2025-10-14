string = input().split()
d = dict()
for i in string:
    d[i] = d.get(i,0) + 1
print(d)
