def reverse(strs: list) -> None:
    """Reverse element of a given string"""
    start, stop = 0, len(strs)
    while start < stop - 1:
        strs[start], strs[stop - 1] = strs[stop - 1], strs[start]
        start += 1
        stop -= 1
