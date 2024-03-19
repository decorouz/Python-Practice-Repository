def mysum(*numbers, start=0):
    """Accept any number of numeric arguments as input.
    Return the sum of those numbers, plus the start value, which default to 0"""

    result = start
    for number in numbers:
        result += number
    return result


print(mysum(10, 20, 30, 40, 9))
