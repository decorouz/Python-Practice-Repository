"""Decorator That Takes an Optional Argument.

You would like to write a single decorator that can be used 
without arguments, such as @decorator, or with optional arguments, 
such as @decorator(x,y,z). However, there seems to be no straightforward 
way to do it due to differences in calling conventions between simple 
decorators and decorators taking arguments
"""

import logging
from functools import partial, wraps


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    """Log Decorator."""
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    log_name = name if name else func.__module__
    log = logging.getLogger(log_name)
    log_msg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, log_msg)
        return func(*args, **kwargs)

    return wrapper


# Example use
@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name="example")
def spam():
    print("Spam!")
