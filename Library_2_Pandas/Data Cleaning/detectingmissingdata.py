import pandas as pd
df=pd.DataFrame({
    "name":["Sanjog","Sujan","Suman","Sushil"],
    "age":[25,30,None,35],
    "city":["Kathmandu","Lalitpur","Bhaktapur",None]
})
print(df)
#1. detecting missing values  
print(df.isnull())#it returns a DataFrame of the same shape as df, where each element is True if the corresponding element in df is missing (NaN) and False otherwise.
print(df.isnull().sum())#it returns a Series containing the count of missing values in each column of the DataFrame. The index of the Series corresponds to the column names, and the values represent the number of missing values in each column.     
print(df.isnull().sum().sum())#it returns the total count of missing values in the entire DataFrame by summing up the counts of missing values from all columns.
#2. detecting duplicate rows
df2=pd.DataFrame({
    "name":["Sanjog","Sujan","Suman","Sushil","Sanjog"],
    "age":[25,30,None,35,25],
    "city":["Kathmandu","Lalitpur","Bhaktapur",None,"Kathmandu"]
})
print(df2)
print(df2.duplicated())#it returns a Series of boolean values indicating whether each row in the DataFrame is a duplicate of a previous row. The first occurrence of a duplicate row is marked as False, while subsequent occurrences are marked as True.
print(df2.duplicated().sum())#it returns the total count of duplicate rows in the DataFrame by summing up the boolean values returned by the duplicated() method. Each True value is counted as 1, so the sum gives the total number of duplicate rows
df2=df2.drop_duplicates()#it removes duplicate rows from the DataFrame, keeping only the first occurrence of each duplicate. The resulting DataFrame will contain only unique rows.
print(df2)
