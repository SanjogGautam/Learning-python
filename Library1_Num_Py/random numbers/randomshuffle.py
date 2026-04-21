import numpy as np

rng = np.random.default_rng()
a = np.arange(1, 13).reshape(3, 4)

print("Original array:")
print(a)

# This modifies 'a' directly and returns None
rng.shuffle(a) 

print("\nShuffled array (modifies original):")
print(a)