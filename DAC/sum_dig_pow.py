import math


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    lst = []
    for num in range(a, b+1):
        if num > 9:
            s = sum_dig(num)
            if s == num:
                lst.append(num)
        else:
            lst.append(num)
    return lst


def sum_dig(num):
    pw = 1
    total = 0
    for dig in str(num):
        total += int(dig)**pw
        pw += 1
    return total


# More clever solution
def is_eureka(num):
    return num == sum(int(digit) ** e for e, digit in enumerate(str(num), 1))


def sum_dig_pow(a, b):
    return [n for n in range(a, b+1) if is_eureka(n)]
