import numpy as np
a=np.array([1,2,3])
print(a.dtype)#int64
#we can also give exclusive datatype as well
b=np.array([1,2,3,4],dtype=float)
print(b)
#typecasting using astype()
d=b.astype(int)
print(d.dtype)