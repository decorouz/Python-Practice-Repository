def convert_int_to_word(num: int) -> str:
    """Convert integer from zero to trillion to its words representation"""
    d = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert 0 <= num, "Non-positive Number Error"

    if num <= 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return f"{d[num // 10 * 10]}-{d[num % 10]}"

    if num < k:
        if num % 100 == 0:
            return f"{d[num//100]} hundred"
        else:
            return f"{d[num//100]} hundred and {convert_int_to_word(num%100)}"
    if num < m:
        if num % k == 0:
            return f"{convert_int_to_word(num // k)} thousand"
        else:
            return f"{convert_int_to_word(num // k)} thousand, {convert_int_to_word(num % k)}"
    if num < b:
        if num % m == 0:
            return f"{convert_int_to_word(num // m)} million"
        else:
            return f"{convert_int_to_word(num // m)} million, {convert_int_to_word(num % m)}"

    if num < t:
        if num % b == 0:
            return f"{convert_int_to_word(num // b)} billion"
        else:
            return f"{convert_int_to_word(num // b)} billion, {convert_int_to_word(num % b)}"

    if num % t == 0:
        return f"{convert_int_to_word(num // t)} trillion"
    else:
        return (
            f"{convert_int_to_word(num // t)} trillion, {convert_int_to_word(num % t)}"
        )


def sort_numbers_by_word_representation(start: int, end: int) -> list[int]:
    """
    Sorts a range of numbers based on the alphabetical order of their word representations.
    """
    results = {}
    for i in range(start, end + 1):
        results[i] = convert_int_to_word(i)
    sorted_int = sorted(results.items(), key=lambda x: x[1])

    sorted_keys = [key for key, _ in sorted_int]
    return sorted_keys


if __name__ == "__main__":
    result = sort_numbers_by_word_representation(10, 100)
    print(result)
