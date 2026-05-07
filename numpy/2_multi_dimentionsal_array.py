import numpy as np

array_1 = np.array('A')

print(f"ARRAY_1 dimensions: {array_1.ndim}")
# shape output:()
print(f"ARRAY_1 shape: {array_1.shape}")


array_2 = np.array(['A', 'B', 'C', 'D'])

print(f"ARRAY_2 dimensions: {array_2.ndim}")
# shape output:(rows)
print(f"ARRAY_2 shape: {array_2.shape}")


array_3 = np.array([['A', 'B', 'C', 'D'],
                   ['E', 'F', 'G', 'H'],
                   ['I', 'J', 'K', 'L']])

print(f"ARRAY_3 dimensions: {array_3.ndim}")
# shape output:(rows, columns)
print(f"ARRAY_3 shape: {array_3.shape}")

# a multidimenstional array should have same number of elements in every list
# or else it will give a error

array_4 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(f"ARRAY_4 dimensions: {array_4.ndim}")
# shape output:(depth/layers, rows, columns)
print(f"ARRAY_4 shape: {array_4.shape}")

print(f"chain indexing: {array_4[0][0][0]}")  # chain indexing
# multidementional indexing is provided by numpy library
print(f"Multidimentional indexing: {array_4[1, 1, 1]}")


word = array_4[1, 1, 2] + array_4[2, 0, 2] + array_4[0, 0, 2] + array_4[0, 2, 1]

print(word)
