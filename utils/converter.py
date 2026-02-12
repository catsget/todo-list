from models import Task


def to_dict(obj: object):
    return obj.__dict__


def to_object(dt: dict):
    return Task(dt["name"], dt["desc"], dt["status"])
