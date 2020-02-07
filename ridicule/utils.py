import inspect


def is_valid_call(function, args, kwargs):
    try:
        inspect.signature(function).bind(*args, **kwargs)
    except TypeError:
        return False
    else:
        return True
