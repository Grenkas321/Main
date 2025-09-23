n = int(input())

i = 0
while i < 3:
    a = n + i
    
    j = 0
    while j < 3:
        b = n + j
        print(a, '*', b, '= ', end='')

        product = a * b

        num = product
        digit_sum = 0
        
        if num == 0:
            digit_sum = 0
        else:
            temp = abs(num)
            while temp > 0:
                digit_sum += temp % 10
                temp = temp // 10
        
        if digit_sum == 6:
            print(':=)', end='')
        else:
            print(product, end='')
        
        if j < 2:
            print(' ', end='')

        j += 1
    
    print()
    i += 1
