import numpy as np
 
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=np.float32)
 
print(a.ndim)      # 2           — number of dimensions
print(a.shape)     # (3, 3)      — (rows, columns)
print(a.size)      # 9           — total number of elements
print(a.dtype)     # float32     — element data type
print(a.itemsize)  # 4           — bytes per element
print(a.nbytes)    # 36          — total bytes (size * itemsize)
print(a.T)#gives the trasnpose of a matrix