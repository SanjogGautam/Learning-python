import numpy as np

rng = np.random.default_rng(seed=1)

# To get integers between 1 and 100:
a = rng.integers(1, 100, size=(2, 2))

# Floats between 5.0 and 10.0
c = rng.uniform(5, 10, size=(2, 2))
print(c)
print(a)
