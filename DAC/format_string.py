def format_address(address_string: str) -> str:
    """Seperates out parts of the address string into new strings

    Args:
        address_string (string): house addresss
    """
    # Declare variables
    house_number = ""
    street_name = ""

    address = address_string.split()

    # Separate the address string into parts

    # Traverse through the address parts
    for part in address:
        if part.isnumeric():
            house_number = part
        else:
            street_name += part
            street_name += " "
    # Determine if the address part is the
    # house number or part of the street name

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return f"house # {house_number} on {street_name}"


def count_letters(text: str) -> dict:
    """Count letters in a text"""
    result = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha() and letter not in result:
            count = text.count(letter)
            result[letter] = count

    return result


if __name__ == "__main__":
    print(
        format_address("123 Main Street")
    )  # "house # 123 on street named Main Street"

    print(format_address("1001 1st Ave"))  # "house # 1001 on street named 1st Ave"

    print(
        format_address("55 North Center Drive")
    )  # "house # 55 on street named North Center Drive"

    print(count_letters("AaBbCc"))  # {'a': 2, 'b': 2, 'c': 2}
    print(
        count_letters("Math is fun! 2+2=4")
    )  # {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
    print(
        count_letters("This is a sentence.")
    )  # {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
