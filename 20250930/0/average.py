def average(*arguments):
    lens = len(arguments)
    summ = sum(arguments)
    return summ / lens

print(average(10, 10, 10, 10, 10))

