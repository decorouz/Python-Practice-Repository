""" Loeschian quadratic form

1729 is the lowest number which can be represented by a Loeschian quadratic form 
 $a^2 + ab+ b^$ in four different ways, with positive integers a and b .
 """


def verify_leoschain_quadratic() -> None:
    """
    1729 is the lowest number which can be represented by a
    Loeschian quadratic form $a^2 + ab+ b^$ in four different ways
    """
    number = 1729
    n = int(number ** (1 / 2))  # half the number of iteration

    results = {}
    for a in range(1, n + 1):
        for b in range(a):
            result = a**2 + a * b + b**2
            if result in results:
                results[result].append((a, b))
            else:
                results[result] = [(a, b)]
            if result > number:
                break
    for x, pairs in results.items():
        if len(pairs) > 3:
            print(f"{x}: {pairs}")


if __name__ == "__main__":
    # Test the function
    verify_leoschain_quadratic()
