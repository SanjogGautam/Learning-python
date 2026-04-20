import pandas as pd
data=[100,102,104]
series=pd.Series(data,index=["Employee1","Employee2","Employee3"])
# we can slice using both iloc and loc
print(series.iloc[0:2])
print(series.iloc[::-1])#print in reverse order
print(series.loc["Employee1":])