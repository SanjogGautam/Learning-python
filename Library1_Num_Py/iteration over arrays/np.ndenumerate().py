import numpy as np
a=np.arange(1,7).reshape(2,3)
for i in np.ndenumerate(a):
    print(i)
    