import pandas as pd
series=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(series)
print(series.index)#it prints the index of the series
print(series.values)#it prints the values of the series
print(series.dtype)#it prints the data type of the series
print(series.shape)#it prints the shape of the series
print(series.size)#it prints the size of the series
print(series.ndim)#it prints the number of dimensions of the series
