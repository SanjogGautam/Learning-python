import numpy as np
rng = np.random.default_rng()

a = np.arange(1, 13)
rng.shuffle(a)          # Shuffle all 12 numbers completely
a = a.reshape(3, 4)     # Then turn them into a grid
print("Fully Shuffled:\n", a)

sorted_a = np.sort(a, axis=1) # Sort each row horizontally
print("\nRows Sorted Horizontally:\n", sorted_a)
sorted_colum=np.sort(a,axis=0)# sorting ieach coloumn
print(sorted_colum)
#np.argsort()- it gives the indices that would sort the arrays
b=np.array([30,10,40,20])
idx=np.argsort(b)
print(idx)
print(b[idx])
