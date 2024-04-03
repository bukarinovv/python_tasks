class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
        
    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')
        
    def __set__(self, obj, value):     
        obj.__dict__[self._attr] = value
        self.count = len(obj.__dict__)
        obj.__dict__[self.count] = value
        
    def get_version(self, obj, n):
        return obj.__dict__[n]
    
    def set_version(self, obj, n):
        obj.__dict__[self._attr] = obj.__dict__[n] 