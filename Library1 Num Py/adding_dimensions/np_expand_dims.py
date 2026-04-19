import numpy as np
a=np.arange(1,7)
print(a)
print(a.shape)
b=np.expand_dims(a,axis=1)#exapand at rows
print(b.shape)
print(b)
c=np.expand_dims(a,axis=0)#expand at columns
print(c.shape)
print(c)