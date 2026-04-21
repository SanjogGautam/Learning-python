import numpy as np
a=np.arange(1,7).reshape(2,3)
print(a)
b=np.arange(1,7)
print(b)
print(b.shape)
#np.newaxis will increase the dimension by 1
b1=b[np.newaxis,:]#adding new axis at row b1
print(b1.shape)
print(b1)
b2=b[:,np.newaxis]#adding new axis at column in b2
print(b2.shape)
print(b2)
