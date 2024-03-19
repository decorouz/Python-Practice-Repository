"""CAPTURING RAINWATER 

Create a capturing_rainwater() function that takes in an array of heights,
and returns the amount of rainwater that could be contained in that array.

For example, the array [4, 2, 1, 3, 0, 1, 2] can be represented in the following histogram: 
Histogram with the Y-axis going from 0 to 4 and the X-axis containing the numbers from the array. 
Water is pooled in the empty spaces of the histogram, and you can see that it can contains 
6 units of water. As you can see, there are 6 units of water that can be contained, so 
capturing_rainwater([4, 2, 1, 3, 0, 1, 2]) will return 6. 
This challenge was reported to have been asked at interviews with many top companies, 
including Amazon and Microsoft. """


def capturing_rainwater(heights: list[int]) -> int:
    """Compute the amount of water that could be contained in a given array

    Parameter
    --------
    heights (list): (n,) array
       list of numbers e.g [4, 2, 1, 3, 0, 1, 2]
    Returns
    -------
    Integer
    """
    water = 0

    n = len(heights)

    # default list to store the max left and max right of each point
    left_max = [0] * n
    right_max = [0] * n

    # Instantiate default right and left max
    left_max[0] = heights[0]
    right_max[n - 1] = heights[n - 1]

    # filling the left_max list
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # filling the right_max list
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # computing the amount of water
    for i in range(n):
        water += min(left_max[i], right_max[i]) - heights[i]

    return water


elevation_height = [4, 2, 1, 3, 0, 1, 3]
print(capturing_rainwater(elevation_height))
