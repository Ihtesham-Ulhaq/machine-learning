import numpy as np

# Aggregate functions = Summerize data and typically
#                       return a single value

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))  # standard daviation
print(np.var(array))  # variation
print(np.min(array))
print(np.max(array))
print(np.argmin(array))  # gives index of min value
print(np.argmax(array))

print(f"sum of columns: {np.sum(array, axis=0)}")
print(f"sum of rows: {np.sum(array, axis=1)}")
