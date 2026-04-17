#np.nditer() is used to iterate over every element and more efficient then nested loops
import numpy as np
a=np.arange(1,7).reshape(2,3)
print(a)
for i in np.nditer(a):
    print(i, end=" ")
for i in np.nditer(a,op_flags='readwrite'):
    i[...]=i*2
print(a)

