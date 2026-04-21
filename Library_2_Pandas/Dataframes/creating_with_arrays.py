import numpy as np
import pandas as pd
# creating a dataframe with arrays
data=np.array([[1,2,3],[4,5,6],[7,8,9]])#it creates a 2D array with the given data
df=pd.DataFrame(data,columns=["A","B","C"])#it creates a dataframe from the 2D array and assigns column names "A", "B", and "C"
print(df)