import pytest


def hex_output():
    """Takes a hex number and returns the decimal equivalent"""
    decnum = 0
    hexnum = input("Enter a hex number to convert: ")
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)


hex_output()
print(hex(80))
