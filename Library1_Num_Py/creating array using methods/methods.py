import numpy as np
a1=np.array(['a','b','c'])
a2=np.zeros(2)#all zeros
a3=np.ones(3)#all ones
a4=np.arange(1,11,2)#range in arrays
print(a1)
print(a2)
print(a3)
print(a4)
#np.full - fills the array with constant value of same
a5=np.full((2,3),5)
print(a5)
#np.eye(creates an identity matrix)
a6=np.eye(3)
print(a6)
#np.empty creates an empty element
a7=np.empty((2,2))
print(a7)
#np.random creates an array of random value
a8=np.random.rand(2,2)#creates a random array of float size 2x2
print(a8)
a9=np.random.randint(1,100,size=(2,3))#creates a random array of integer size 2X2
print(a9)