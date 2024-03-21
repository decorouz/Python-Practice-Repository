"""Binary search as an algorithm.

Its input is a sorted list of items. 
There are three possible senarios to find the element in a list
    - search criteria = middle item
    - search criteria < middle item: search the first half of the array
    - search criteria > middle item: search the upper half of the array

"""

from typing import List


def binary_search(items: List[int], target: int) -> int | None:
    """Iterative Binary search

    Parameters
    ----------
    items: List
        A list of items
    target:
        Search criteria

    Returns
    -------
    index: int
        Target element index
    """
    sorted(items)
    left, right = 0, len(items) - 1
    while left < right:
        mid = (left + right) // 2
        potential_match = items[mid]
        if target == potential_match:
            return mid
        if target < potential_match:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Big O notation tells you how fast an algorithm is.
# Suppose you have a list of size n. Simple search needs to check
# each element, so it wll take n operations. The run time is O(n).
# Where n is the number of operations.


def binary_search_with_recur(item_list: List[int], target: int) -> int | None:
    """Recursive binarys search

    Parameters
    ----------
    items: List
        A sorted list of integers
    target:
        An item to be located in the sorted list
    Returns
    -------
    index: int
        Index of target item
    """
    items = sorted(item_list)  # ensure the list is sorted
    if not items:
        return None
    left, right = 0, len(items) - 1
    mid_idx = (left + right) // 2
    potential_match = items[mid_idx]

    if potential_match == target:
        return mid_idx

    if target < potential_match:
        left_half = items[:mid_idx]
        return binary_search_with_recur(left_half, target)
    if target > potential_match:
        right_half = items[(mid_idx + 1) :]
        result = binary_search_with_recur(right_half, target)

        if result is None:
            return result
        return result + mid_idx + 1


# Driver code
if __name__ == "__main__":
    ITEM = 9
    arr = [13, 14, 15, 16, 17, 9]  # Unsorted list
    # print(binary_search(arr, ITEM))
    print(binary_search_with_recur(arr, target=ITEM))
