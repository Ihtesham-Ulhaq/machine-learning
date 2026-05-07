import numpy as np

# print(np.__version__)

# normal list behaviour

list = [1, 2, 3, 4]
print(list * 2)

# list in form of array behaviour
# its faster and works like C language
array = np.array([1, 2, 3, 4])
array *= 2
print(array)


# numpy library is superior to python
# as it follows c language logic which is
# of closer to machine and much faster
