def itemget(collection, index):
    return collection[index]

def safeindex(function, *args):
    try:
        return function(*args)
    except IndexError:
        return None

print([safeindex(itemget, "qwe", i) for i in range(5)])

try:
    print(safeindex(itemget, "qwe", "qwe"))
except TypeError as e:
    print("TypeError не перехвачен:", e)
