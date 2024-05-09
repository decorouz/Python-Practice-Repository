"""Write a short python script with While lop to check if a string is a
palindrome. That is, it is equal to its reverse. 
For example, `racecar` and `gohangasalamiimalasagnahog` are palindromes.
"""


def is_palindrome(string: str) -> bool:
    if string[0] != string[-1]:
        return False

    left, right = 0, len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    input_str = "gohangasalamiimalasagnahog"
    input_str2 = "racecar"
    palendrome1 = is_palindrome(input_str)
    palendrome2 = is_palindrome(input_str2)
    print(palendrome1)
    print(palendrome2)
