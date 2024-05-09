# Decorator with wrap


import time
from functools import wraps
from math import sqrt
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
def pythogoras_theorem(n):
    """Does some math"""
    for a in range(1, n + 1):
        for b in range(a, n):
            c_square = a**2 + b**2
            c = int(sqrt(c_square))
            if (c_square - c**2) == 0:
                print(a, b, c)


pythogoras_theorem(35)
