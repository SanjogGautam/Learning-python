import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")
# 3. Correcting data types
# data types can be corrected by using the astype() method, which allows you to convert a column to a specific data type.
# a. Converting a column to a specific data type
df["Legendary"]=df["Legendary"].astype(bool)#it converts the "Height" column to a float data type
print(df.dtypes)
# b. Converting multiple columns to specific data types
df[["Height","Weight"]]=df[["Height","Weight"]].astype(float)#it converts the "Height" and "Weight" columns to float data types
print(df.dtypes)