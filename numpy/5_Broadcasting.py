import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger arrays shape.

# the dimensions have the same size.
# OR
# one of the dimension has a size of 1
# read dimension from right to left

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1],
                   [2],
                   [3],
                   [4]])

print(array1.shape)
print(array2.shape)
# they are compatible bcz one of dimension from
# each row and columns was 1
# (1, 4)
# (4, 1)
# works same as matrix
print(array1 * array2)
print()
print()
print()

array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
array4 = np.array([[1],
                   [2],
                   [3],
                   [4]])

print(array3.shape)
print(array4.shape)
# (2, 4)
# (4, 1)
# print(array3 * array4)  # error as they are not compatible
print()
print()
print()

array5 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
array6 = np.array([[1],
                   [2],
                   [3],
                   [4]])

print(array5.shape)
print(array6.shape)
# (4, 4)
# (4, 1)
print(array5 * array6)
print()

# EXCERCISE

print("----------------EXCERCISE----------------")

arr1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arr2 = np.array([[1],
                 [2],
                 [3],
                 [4],
                 [5],
                 [6],
                 [7],
                 [8],
                 [9],
                 [10]])

print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)
