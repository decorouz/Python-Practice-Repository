import string

# My solution


def is_pangram(s):
    alphabets = string.ascii_lowercase
    unique_chars = set([char.lower() for char in s if char.isalpha()])
    for char in unique_chars:
        if alphabets.count(char) == 1 and len(unique_chars) == 26:
            return True
        else:
            return False


# Most clever solution online
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))
