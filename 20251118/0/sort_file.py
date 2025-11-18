
with open('o', 'w+') as file:
    print('Wasup bro!\n Im Vlad!\n', file = file)
with open('o', 'r+') as file:
    print(sorted(file.readlines()))
