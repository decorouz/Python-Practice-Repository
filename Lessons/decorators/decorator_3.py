"""Decorator.

A decorator is a function that accepts a function as input and returns
a new function as output.
"""
import logging
import time
from functools import wraps


# You want to put a wrapper layer around a function that adds
# extra processing.
def time_this(func):
    """Decorate that reports the execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@time_this
def count_down(n):
    """Count down."""

    while n > 0:
        n -= 1


# Example Use
if __name__ == "__main__":
    count_down(100000)


# Defining a Decorator That Takes Arguments.
# -----------------------------------------
# Suppose you want to write a decorator that add logging to a function,
# but allows user to specify the logging level and other details as args.
def logged(level, name=None, message=None):
    """Add logging to a function.

    if name and message aren't specified, the default
    to the function's module and name.
    Parameters
    ----------
    level
        The logging level
    name, optional
        Logger name.
    message, optional
        Log message.
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


# # Example Use
# if __name__ == "__main__":
#
#     @logged(logging.DEBUG)
#     def add(x, y):
#         return x + y
#
#     @logged(logging.CRITICAL, "example")
#     def spam():
#         print("Spam!")
