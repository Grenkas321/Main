print(*(sorted(args := list(eval(input())), key = lambda x: (x**2)%100)))

