"""Defining Decorators As Part of a Class.

You want to defind decorator inside a class definition and apply
it to other functions or method.
"""
from functools import wraps


class A:
    def decorator1(self, func):
        """Decorator as an instance method."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, func):
        """Decorator as a class method."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)

        return wrapper


# Example use case
a = A()


@a.decorator1
def spam():
    print("Spam!")


# As a class method
@A.decorator2
def grok():
    pass


spam()
