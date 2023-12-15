"""Selection Sort.

Suppose you have a bunch of music on your computer.
For each artist, you have a play count. 
You want to sort this list from most to least played.
"""


def find_smallest(arr: list[int]) -> int:
    """Find the index of smallest element in an array.

    Parameters
    ----------
    arr: Array
        Array of real numbers
    Return:
    -------
    smallest_index: int
        The index of the smallest element
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
