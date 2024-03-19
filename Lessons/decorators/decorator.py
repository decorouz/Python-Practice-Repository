from typing import Callable, TypeVar, Awaitable

R = TypeVar("R")


def logged(function: Callable[..., R]) -> Callable[..., R]:
    def wrapper(*args: object, **kwargs: object):
        value = function(*args, **kwargs)
        with open("logfile.txt", "a+") as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return fname

    return wrapper


# @logged
# def add(x, y):
#     return x + y

# add(1, 3)

# Another practical example of decorators
# Defining decorators that takes arguements
import logging
from functools import wraps


def logged2(level, name=None, message=None):
    """Add logging to a function

    Args:
        level (_type_): logging level
        name (_type_, optional): logger name. Defaults to None.
        message (_type_, optional): log message. Defaults to None.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__


        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged2(logging.DEBUG)
def add(x, y):
    return x + y


@logged2(logging.CRITICAL, "example")
def spam(x, y):
    print("spam!")
    
spam(3,5)