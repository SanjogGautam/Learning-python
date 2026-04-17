#its main aim is to wrap a regular python functio so it can be applied element wise toa numpy array
import numpy as np
def odd_even(x):
    return 'odd' if x%2!=0 else 'even'
b=np.vectorize(odd_even)
a=np.array([1,2,3,4,5])
print(b(a))