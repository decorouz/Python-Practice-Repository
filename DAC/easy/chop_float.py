def chop_float(float_num: float, before: int, after: int) -> float:
    """A function that takes a float and two integers.
    Returns a float consisting of before digits before
    the decimal point and after digits after
    """
    # before
    str_truncate = str(int(float_num))
    str_truncate = str_truncate[-before:]
    str_float = float(str_truncate)
    # after
    number_dec = float_num - int(float_num)
    number_dec = str(number_dec)
    number_dec = number_dec[0 : after + 2]

    return str_float + float(number_dec)


print(chop_float(1234.5678, 2, 3))
