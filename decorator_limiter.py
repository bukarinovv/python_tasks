def limiter(limit, unique, lookup):
    def decorator(cls):
        cls.ex = {}
        cls.limit = limit
        def foo(*args, **kwargs):
            obj = cls(*args, **kwargs)
            if obj.__dict__[unique] not in cls.ex:
                if cls.limit > 0:
                    cls.ex[obj.__dict__[unique]] = obj
                    cls.limit -= 1
                    return obj
                elif lookup == 'FIRST':
                    obj = list(cls.ex.values())[0]
                    return obj
                elif lookup == 'LAST':
                    obj = list(cls.ex.values())[-1]
                    return obj
            else:
                obj = cls.ex[obj.__dict__[unique]]
                return obj
        return foo
    return decorator