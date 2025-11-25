class Doubleton(type):
    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)
        cls._instances = []
        cls._idx = 0

    def __call__(cls, *args, **kwargs):
        if len(cls._instances) < 2:
            inst = super().__call__(*args, **kwargs)
            cls._instances.append(inst)
        inst = cls._instances[cls._idx]
        cls._idx = (cls._idx + 1) % len(cls._instances)
        return inst

