import numpy as np

# Filtering = Refers to the process of selecting elements
#             from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])


teenagers = ages[ages < 18]
print(f"Teenagers: {teenagers}")
adults = ages[(ages >= 18) & (ages < 65)]
print(f"Adults: {adults}")
seniors = ages[ages >= 65]
print(f"Seniors: {seniors}")

evens = ages[ages % 2 == 0]
print(f"Evens: {evens}")

odds = ages[ages % 2 != 0]
print(f"Odds: {odds}")

# to keep the original shape of array 
# where(Condition, [x, y]/array, value which will replace the values if condition is false)
# can be replaced in anything but to remove or show this element
# not available or part of array we use 
# 0
# -1
# np.nan(not a number)
adults = np.where((ages >= 18) & (ages < 65), ages, 0)
print(f"Adults: {adults}")
