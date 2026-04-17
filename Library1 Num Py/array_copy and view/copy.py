import numpy as np
original = np.array([1, 2, 3, 4, 5])
 
copy = original.copy()    # explicit deep copy
copy[0] = 99
 
print(original)            # [1 2 3 4 5]  — unchanged
print(copy)                # [99 2 3 4 5]
 
print(copy.base is None)   # True — owns its own data
