import numpy as np
a=np.arange(1,13)
print(a)
b=a.reshape(3,4)#2d
c=a.reshape(2,2,3)#3d
print(b)
print(c)
d=b.flatten()#reshpae to 1 dimension
print(d)
