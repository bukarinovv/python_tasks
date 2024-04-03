from functools import wraps

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            one = dict(zip(args, self.types))
            if all(map(lambda x: type(x) is one[x], one)):
                return func(*args, **kwargs)
            raise TypeError
        return wrapper 