import numpy as np

# Create a rank 2 array with shape (3, 4)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
b = a[:2, 1:3]
b.shape  # (2,2)


# Two ways of accessing the data in the middle row of the array. Mixing integer indexing with slices yields an array of lower rank, while
# using only slices yields an array of the same rank as the original array:

row_r1 = a[1, :]  # rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
row_r3 = a[[1], :]  # Rank 2 view of the second row of a

print(row_r1, row_r1.shape)  # [5 6 7 8] (4,)
print(row_r2, row_r2.shape)  # [[5 6 7 8]] (1, 4)
print(row_r3, row_r3.shape)  # [[5 6 7 8]] (1, 4)


# We can make some distinctions when accessing the columns of an array
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]

print(col_r1, col_r1.shape)  # [ 2  6 10] (3,)

print(col_r2, col_r2.shape)  # [[ 2][ 6] 10]] (3, 1)

# Integer array indexing: Allows you contruct arbitrary array using data from another array
# Here is an example

a_1 = np.array([[1, 2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a_1[0, 1, 2], [0, 1, 0])  # [1 4 5]

# The above example of integer array indexing is equivalent to this:
print(np.array([a_1[0, 0], a_1[1, 1], a_1[2, 0]]))

######################################################################################

# Selecting and mutating one element from each row of a matrix
# Create a new array from which we will select elements
a_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Create an array of indices
b_2 = np.array([0, 2, 0, 1])

# select one element from each row of a_2 using the indices of b_2
print(a_2[np.arange(4), b_2])  # Prints "[ 1  6  7 11]"

# Mutating one element from each row of a_2 using the indices in b_2
a_2[np.arange(4), b_2] += 10
print(a_2)


####################
a_3 = np.zeros(4)
print(a_3)