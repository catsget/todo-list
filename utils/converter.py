class Obj:
    pass

def to_dict(obj: object):
    return obj.__dict__

def to_object(dt: dict):
    obj = Obj()
    for key, value in dt.items():
        setattr(obj, key, value)
    return obj