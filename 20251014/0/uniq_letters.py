from string import ascii_lowercase
set_g = {'a','e','i','u','o','y'}
set_s = set(ascii_lowercase) - set_g

string = set(input())
print(len(set_s & string), len(set_g & string))
