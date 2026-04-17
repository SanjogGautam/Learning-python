import numpy as np
a=np.arange(1,13).reshape(3,4)
print(a)
#printing every row
for row in a:
    print(row)
#for printing every element
for row in a:
    for value in row:
        print(value,end="")