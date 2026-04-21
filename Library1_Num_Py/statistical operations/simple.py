import numpy as np
 
data = np.array([4, 8, 15, 16, 23, 42])
 
print(np.sum(data))          # 108   — sum of all elements
print(np.mean(data))         # 18.0  — arithmetic mean
print(np.median(data))       # 15.5  — middle value
print(np.min(data))          # 4     — minimum
print(np.max(data))          # 42    — maximum
print(np.std(data))          # 12.33 — standard deviation
print(np.var(data))          # 152 — variance
print(np.percentile(data,75))# 21.25 — 75th percentile
print(np.ptp(data))          # 38    — peak to peak (max - min)

new=np.array(((1,2,3),
             (4,5,6)))
print(np.argmax(new))#it gives the position of maximum value
print(np.argmin(new))#it gives th position of minimum value
print(np.sum(new,axis=0))#it gives the sum of the columns
print(np.sum(new,axis=1))#it gives the sum of the rows
 