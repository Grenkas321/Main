sum = 0

while sum <= 21:
    num = int(input())
    sum += num
    if num <= 0:
        print(num)
        break
else:
    print(sum)
