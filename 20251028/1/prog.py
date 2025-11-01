class Omnibus:
    __counters = {}
    __attributes = {}

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
            return
            
        obj_id = id(self)
        
        if obj_id not in self.__attributes or name not in self.__attributes[obj_id]:
            Omnibus.__counters[name] = Omnibus.__counters.get(name, 0) + 1
            
            if obj_id not in self.__attributes:
                self.__attributes[obj_id] = set()
            self.__attributes[obj_id].add(name)

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
        
        return Omnibus.__counters.get(name, 0)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
            return
            
        obj_id = id(self)
        
        if obj_id in self.__attributes and name in self.__attributes[obj_id]:
            if name in Omnibus.__counters:
                Omnibus.__counters[name] -= 1
                if Omnibus.__counters[name] == 0:
                    del Omnibus.__counters[name]
            
            self.__attributes[obj_id].remove(name)

import sys
exec(sys.stdin.read())