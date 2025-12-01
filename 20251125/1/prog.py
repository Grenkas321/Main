from functools import wraps
import inspect

class dump(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        for attr, value in list(namespace.items()):
            if inspect.isfunction(value):
                func = value

                @wraps(func)
                def wrapper(self, *args, __func=func, **kwargs):
                    print(f"{__func.__name__}: {args}, {kwargs}")
                    return __func(self, *args, **kwargs)

                namespace[attr] = wrapper
        return super().__new__(mcls, name, bases, namespace)


import sys
exec(sys.stdin.read())
