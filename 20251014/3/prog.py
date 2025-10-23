from collections import Counter

W = int(input())
words = Counter()

while s:=input():
    new_s = ''
    for i in s.lower():
        if i.isalpha():
            new_s += i
        else:
            new_s += ' '
    new_s = [i for i in new_s.split() if len(i) == W]
    words.update(new_s)

if not words:
    exit()

maxim = words[words.most_common()[0][0]]
print(' '.join(sorted([i for i in words.keys() if words[i] == maxim])))
