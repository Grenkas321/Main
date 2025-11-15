from collections import UserString

class DivStr(UserString):
    def __init__(self, seq=""):
        super().__init__(seq)

    def __floordiv__(self, num: int):
        num = int(num)
        if num <= 0:
            raise ValueError("num must be a positive integer")
        size = len(self.data) // num
        s = self.data
        def gen():
            for i in range(num):
                yield self.__class__(s[i*size:(i+1)*size])
        return gen()

    def __mod__(self, num: int):
        num = int(num)
        if num <= 0:
            raise ValueError("num must be a positive integer")
        r = len(self.data) % num
        return self.__class__("" if r == 0 else self.data[-r:])

import sys
exec(sys.stdin.read())