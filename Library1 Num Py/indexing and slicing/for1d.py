import numpy as np
a = np.array([10, 20, 30, 40, 50])

 
print(a[0])        # 10   — first element
print(a[-1])       # 50   — last element
print(a[1:4])      # [20 30 40]
print(a[:3])       # [10 20 30]
print(a[2:])       # [30 40 50]
print(a[::2])      # [10 30 50]  — every 2nd element
print(a[::-1])     # [50 40 30 20 10]  — reversed
