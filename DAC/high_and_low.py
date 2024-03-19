def high_and_low(numbers: str):
    """Given a string of space seperated numbers.
    return the highest and lowest number from the string
    """
    # convert to int
    numbers = [int(x) for x in numbers.split(" ")]
    return f"{max(numbers)} {min(numbers)}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
# high_and_low("1 2 3 4 5")
# high_and_low("1 9 3 4 -5")
