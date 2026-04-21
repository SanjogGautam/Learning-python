#similar to python range but returns numpy array
#np.arrange(start,stop,step,dtype)
import numpy as np
# Integers
print(np.arange(10))           # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(2, 10))        # [2 3 4 5 6 7 8 9]
print(np.arange(0, 20, 3))     # [ 0  3  6  9 12 15 18]
print(np.arange(10, 0, -2))    # [10  8  6  4  2]
 
# Float step
print(np.arange(0, 1, 0.2))    # [0.  0.2 0.4 0.6 0.8]
