import numpy as np
a = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12]])
 
# Single element — [row, col]
print(a[0, 0])         # 1
print(a[1, 2])         # 7
print(a[-1, -1])       # 12
 
# Entire row
print(a[1])            # [5 6 7 8]
print(a[1, :])         # [5 6 7 8]
 
# Entire column
print(a[:, 2])         # [3 7 11]
 
# Sub-matrix — rows 0-1, cols 1-2
print(a[0:2, 1:3])
# [[2 3]
#  [6 7]]
 
# Every other row, every other column
print(a[::2, ::2])
# [[ 1  3]
#  [ 9 11]]
