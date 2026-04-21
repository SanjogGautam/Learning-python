import numpy as np
a=np.array([4,2,1,5,23,11,3])
#np.sort()returs a sorted copy of an array
print(np.sort(a))
print(np.sort(a)[::-1])#sorting in reverse / descending order 
print(a)#The original array is unaffected
