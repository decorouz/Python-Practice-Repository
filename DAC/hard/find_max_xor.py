"""This problem was asked by Salesforce.

Given an array of integers, find the maximum XOR of any two elements.
"""


def find_max_xor(nums: list[int]) -> int:
    """Compute maximum XOR; naive approach.

    Calculate the XOR for each pair of element in an array.
    Parameters
    ----------
    nums: array
        Given array of non negative integers
    Returns
    -------
    maximum_xor: Decimal
        Bitwise maximum of XOR of any two elements in `nums`
    """
    max_xor = 0

    for _, elem1 in enumerate(nums):
        for _, elem2 in enumerate(nums, 1):
            max_xor = max(max_xor, elem1 ^ elem2)
    return max_xor


# Driver code
if __name__ == "__main__":
    arr = [25, 10, 2, 8, 5, 3]
    print(find_max_xor(arr))  # 28
