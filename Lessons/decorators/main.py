# Decorator with wrap


import time
from functools import wraps
from typing import Callable, TypeVar

from typing_extensions import ParamSpec

P = ParamSpec("P")
T = TypeVar("T")


def timeit(func: Callable[P, T], *args, **kwargs) -> Callable[P, T]:
    """Custom decorator to compute function run time"""

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f"Function {func.__name__}{args}{kwargs} took {total_time:.2f} seconds to run"
        )
        return result

    return timeit_wrapper


@timeit
def add(x, y):
    """Does some math"""
    return x + y


add(1, 2)
