"""Write a short python script with While lop to check if a string is a
palindrome. That is, it is equal to its reverse. 
For example, `racecar` and `gohangasalamiimalasagnahog` are palindromes.
"""


def is_palindrome(strs: str) -> bool:
    """Determine if string is palindrome"""
    if strs[0] != strs[-1]:
        return False
    left, right = 0, len(strs) - 1
    while left < right:
        if strs[left] != strs[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    input_str = "gohangasalamiimalasagnahog"
    input_str2 = "racecar"
    result1 = is_palindrome(input_str)
    result2 = is_palindrome(input_str2)
    print(result1)
    print(result2)
