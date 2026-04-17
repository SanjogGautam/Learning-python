import numpy as np
array=np.array([[['a'],['b'],['c']],
                [['d'],['e'],['f']],
                [['f'],['g'],['h']]])
print(array.ndim)
print(array.shape)
print(array[0][0][0])#chain accessing
print(array[0,0,0])#multidimensional indexing
print(array[1,0,0])#gives d
