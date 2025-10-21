def travel(n):
    y = yield from n * ['по кочкам']
    return "и в яму       !!!БУХ!!!"

def travelwrap(n):
    yield (yield from travel(n))
