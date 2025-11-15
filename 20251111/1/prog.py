from functools import wraps

def objcount(cls):
    cls.counter = 0

    orig_init = getattr(cls, "__init__", None)
    orig_del  = getattr(cls, "__del__",  None)

    @wraps(orig_init) if callable(orig_init) else (lambda f: f)
    def _init(self, *args, **kwargs):
        if orig_init is not None:
            orig_init(self, *args, **kwargs)
        cls.counter += 1

    def _del(self):
        cls.counter -= 1
        if orig_del is not None:
            try:
                orig_del(self)
            except Exception:
                pass

    cls.__init__ = _init
    cls.__del__  = _del
    return cls

import sys
exec(sys.stdin.read())