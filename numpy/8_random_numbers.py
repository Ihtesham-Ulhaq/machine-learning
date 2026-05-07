import numpy as np

rng = np.random.default_rng(seed=45)
# seed= will produce the results and then for every seed will show
# the same result as it as before
print(rng.integers(low=0, high=7, size=(3, 2)))

np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(10, 3)))

rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

rng = np.random.default_rng()

fruits = np.array(["🍎", "🍌", "🍍", "🍊", "🥥"])
fruit = rng.choice(fruits)
print(fruit)
fruits = rng.choice(fruits, size=2)
print(fruits)
fruits = rng.choice(fruits, size=(3, 2))
print(fruits)