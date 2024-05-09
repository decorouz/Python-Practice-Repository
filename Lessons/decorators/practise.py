from functools import wraps
from typing import Callable


def uppercase_decorator(func: Callable[[str], str]) -> Callable:
    @wraps(func)
    def wrapper(*args: str, **kwargs: str) -> str:
        result: str = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name: str) -> str:
    """Greets a user"""
    return f"Hello {name}"


print(greet("James"))
print(greet.__name__)
print(greet.__doc__)
