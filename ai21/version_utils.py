import warnings
from functools import wraps

V3_DEPRECATION_MESSAGE = "This model is not supported anymore - Please upgrade to v3.0.0"


def deprecated(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    return decorator
