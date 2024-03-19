from decimal import Decimal as D


def floating_point_sum(str1, str2) -> D:
    """A function that takes two string from the user,
    turns them into decimal instances,
    and then print the floating-point su of the users two inputs
    """

    if isinstance(str1, (str)) and isinstance(str2, (str)):
        return D(str1) + D(str2)

    return D(str(str1)) + D(str(str2))


print(floating_point_sum("0.1", "0.2"))
