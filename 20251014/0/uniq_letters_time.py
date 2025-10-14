from string import ascii_lowercase
import timeit

def letter_time(s):
    string = set(s)
    set_g = {'a','e','i','u','o','y'}
    set_s = set(ascii_lowercase) - set_g

    return(len(set_s & string), len(set_g & string))


s = input()
print(timeit.Timer("letter_time(s)", globals = globals()).autorange())
