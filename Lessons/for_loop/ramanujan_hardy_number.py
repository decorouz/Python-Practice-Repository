"""Ramanujan-Hardy number"""

# number 1729: The smallest number expressible as the sum of two cubes in two different ways."
# For this reason 1732 is known as the Ramanujan-Hardy number.

# ? Can you verify this with a Python program?

import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        endtime = time.perf_counter()
        total_time = endtime - start_time
        print(
            f"Function {func.__name__} with the following args {args}{kwargs} took {total_time} seconds to run"
        )
        return result

    return wrapper


@time_it
def verify_ramanujan_hardy_number() -> None:
    """Verify that 1732 is a Ramanujan-Hardy number"""

    number = 1729
    n = int(number ** (1 / 3))

    cubes = {}  # ? Why did we save in dictionary
    for i in range(1, n + 1):
        for j in range(i):
            result = i**3 + j**3
            if result in cubes:
                cubes[result].append((i, j))
            else:
                cubes[result] = [(i, j)]
            if result > number:
                break
    for cube_sum, pair in cubes.items():
        if len(pair) > 1:
            print(f"{cube_sum}: {pair}")


if __name__ == "__main__":
    # Test the function
    verify_ramanujan_hardy_number()
