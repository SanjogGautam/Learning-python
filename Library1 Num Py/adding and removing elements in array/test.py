import numpy as np
a=np.arange(1,4)
a1=np.resize(a,(2,6))#If the elements are not there it will repeat the elements
print(a1)
#append()-it gives flatten array
b=np.array([[1,2,3],
            [4,5,6]])
print(a1.shape,b.shape)
z=np.append(a1,b)
print(z)
#inserting elements in an array
print(a)
a=np.insert(a,[1],[8,9])
print(a)
#deleting an element of the array
a=np.delete(a,0)
print(a)