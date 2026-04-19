import numpy as np
#where is used while searching 
a = np.array([5, 15, 25, 35, 45])
 
# Find indices where condition is True
idx = np.where(a > 20)
print(idx)                  # (array([2, 3, 4]),)
print(a[idx])               # [25 35 45]
 
# Replace values conditionally
result = np.where(a > 20, a, 0)
print(result)               # [ 0  0 25 35 45]
 
# np.where(condition, value_if_true, value_if_false)
labels = np.where(a % 2 == 0, "even", "odd")
print(labels)
