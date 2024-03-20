# Decorator without wrap


import time
from functools import wraps


def timeit(func, *args, **kwargs):
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
    return x + y


add(1, 2)
