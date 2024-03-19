def mysum(*numbers):
    """Accepts any number of numeric arguement as input.
    Return the sum of those numbers.
    If invoked without an arguement, returns 0"""

    result = 0
    for number in numbers:
        result += number
    return result


print(mysum(10, 20, 30, 40))
