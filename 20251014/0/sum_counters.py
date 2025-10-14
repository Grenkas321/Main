from collections import Counter

s1 = Counter(input().split())
s2 = Counter(input().split())
for i in s2.keys():
    if s1[i] < s2[i]:
        print(False)
        break
else:
    print(True)
