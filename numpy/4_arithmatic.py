import numpy as np

# Scalar arithmatic

array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)


# Vectorized math func

array_2 = np.array([1.01, 2.5, 3.99])

# print(np.sqrt(array))
# print(np.round(array_2))  # round to closest int
# print(np.floor(array_2))  # round down
# print(np.ceil(array_2))  # round up (ceil = ceiling)
# print(np.pi)

# EXERCISE
radii = np.array([1, 2, 3])

print(np.pi * (radii ** 2))

# Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 ** array2)

# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)