import numpy as np
original = np.array([1, 2, 3, 4, 5])
 
view = original[1:4]   # slicing returns a VIEW
print(view)            # [2 3 4]
 
view[0] = 99           # modifying view...
print(original)        # [1 99 3 4 5]  — original ALSO changed!
 
# Check if array owns its data
print(view.base is original)   # True — it is a view
#reshape() is a also a view
a = np.array([1, 2, 3, 4, 5, 6])
 
b = a.reshape(2, 3)
b[0, 0] = 99
 
print(a)   # [99  2  3  4  5  6]  — reshape returns a VIEW
