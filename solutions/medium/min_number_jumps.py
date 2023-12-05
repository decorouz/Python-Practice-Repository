"""Extract the minimum number of jumps.

You are given an array of integers, where each element represents the 
maximum number of steps that can be jumped going forward from that element. 
Write a function to return the minimum number of jumps you must take in
order to get from the start to the end of the array.

For example, given [6, 6, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, 
as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
"""

# Think of the problem with an array of length 2


# Solution 1
def min_jumps(arr: list[int]) -> int:
    """Compute the minimum number of jumps

    Parameters
    ----------
    arr : list[int]
        list of integers

    Returns
    -------
    int
        The maximum number of jumps
    """

    if not arr and len(arr) == 0:
        return 0

    max_reach = arr[0]  # maximum reachable index
    steps = arr[0]
    jumps = 1

    for start in range(1, len(arr)):
        if start == len(arr) - 1:
            return jumps

        max_reach = max(max_reach, start + arr[start])
        steps -= 1

        if steps == 0:
            jumps += 1

            if start >= max_reach:
                return -1  # When nothing is reachable from a give source

            steps = max_reach - start  # Number of steps without jumping
    return -1


# Driver program to test above function

# Driver Program to test above function

if __name__ == "__main__":
    arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr2 = [6, 2, 4, 0, 5, 0, 5, 1, 1, 4, 2, 0, 1, 0, 2, 9]
    arr3 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(min_jumps((arr2)))
