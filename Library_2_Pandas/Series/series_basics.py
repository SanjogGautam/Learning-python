import pandas as pd
#series is a pandas 1-d labeled array that can hold any data type
#it is like a single column in a spreadsheet
data=[100,102,104]
series=pd.Series(data,index=["Employee1","Employee2","Employee3"],dtype=float)#Series() is a constructor that is used in this program to create a series
print(series)
#accessing using .loc- location by label and .iloc by index
print(series.loc["Employee1"])
print(series.iloc[1])
series["Employee4"]=106#inserting data
print(series)
del series["Employee1"]#this deltes employee 1
series= series.drop(series.index[1])
print(series)
