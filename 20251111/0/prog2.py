def istype(typ):
    def deco(fun):
        def newfun(*args):
            if not all(isinstance(arg, typ) for arg in args):
                raise TypeError(f"What's this SHIT, I need {typ}!")
            return fun(*args)
        return newfun
    return deco

@istype(int)
def isit(N):
    return 2*N + 1
    

