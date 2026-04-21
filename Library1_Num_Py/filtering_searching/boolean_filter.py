import numpy as np
a=np.arange(1,13).reshape(3,4)
print(a[a>5])#it retuns a flatten shape 
# to actually give true and false value s we can use
print(a>5)
#for finding the index of minimum and maximum elements is given by
print(np.argmax(a))
print(np.argmin(a))
#np.searchsorted() — Binary Search
#Find index where a value should be inserted to keep a sorted array sorted.
#print(np.searchsorted(a,1))#this will throw an error because it only workes on 1d array