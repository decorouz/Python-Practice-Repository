"""The maximum of two numbers.

Find the maximum of two numbers without using any if-else 
statements, branching, or direct comparisons.
"""


def find_max(x: int, y: int) -> int:
    """Compute the max of two numbers with bitwise operator.

    The generalize formula to find the max with absolute value
    max = (x+y + ABS(x-y))/2
    Parameters
    ----------
    x,y: int
        Given interger values

    Returns
    -------
    Max between x and y.

    Reference
    ---------
    .. [1] Bit Twiddling Hacks, S.E Anderson, 2005
        http://graphics.stanford.edu/~seander/bithacks.html#IntegerMinOrMax
    """
    r = x ^ ((x ^ y) & -(x < y))
    return r


# Driver Code
if __name__ == "__main__":
    print(find_max(2, 3))  # 3
    # print(find_max(2, -3))  # 2
    # print(find_max(-2, -3))  # -2
