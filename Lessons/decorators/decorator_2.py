"""Defining Decorators with User Adjustable Attributes.

You want to write a decorator function that wraps a function,
but has user adjustable attributes that can be used to control
the behavior of the decorator at runtime.

Accessor functions: Changes internal variables through the use of
    nonlocal variable declarations.

Example
-------
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> add(2,3)
DEBUG:__main__:add
5
>>> # Change the log message
>>> add.set_message("Add Called")
>>> add(2,3)
DEBUG:__main__:Add Called
5
>>> # change log level
>>> add.set_level(logging.WARNING)
>>> add(2,3)
WARNING:__main__:Add Called
5
"""
import logging
from functools import partial, wraps


def attach_wrapper(obj, func=None):
    """Add Utility decorator.

    To attach a function as an attribute of obj.
    """
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """Add logging to a function.

    Parameters
    ----------
    level
        Logging level
    name, optional
        Logger name
    message, optional
        Log message
    """

    def decorate(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_msg):
            nonlocal log_msg
            log_msg = new_msg

        return wrapper

    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def spam():
    print("Spam")
