"""Class decorators are usually used to maintain a state."""

# eg. keeping track of the number of times a function is called.

from functools import update_wrapper
from typing import Any, Callable


class CountCalls:
    """Custom decorator to keep track of function calls"""

    def __init__(self, func: Callable[..., Any]) -> None:
        update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # Extend functionality, execute function and return result
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.num_calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(num):
    print("Hello")


say_hello(5)
