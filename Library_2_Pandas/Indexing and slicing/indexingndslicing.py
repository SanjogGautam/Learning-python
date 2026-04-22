import pandas as pd
df = pd.read_csv('data.csv', index_col="Name")
#1. indexing and slicing
# a. indexing
print(df["Type1"])#it returns a Series containing the values of the "Type1" column. The index of the Series corresponds to the index of the DataFrame, and the values represent the data in the "Type1" column.
print(df[["Type1","Type2"]])#it returns a DataFrame containing the values of the "Type1" and "Type2" columns. The index of the DataFrame corresponds to the index of the original DataFrame, and the columns represent the selected columns.
# b. slicing
print(df[0:5])#it returns a DataFrame containing the first 5 rows of the original DataFrame. The index of the returned DataFrame corresponds to the index of the original DataFrame, and all columns are included.
print(df.loc["Bulbasaur"])#it returns a Series containing the values of the row with the index label "Bulbasaur". The index of the Series corresponds to the column names of the DataFrame, and the values represent the data in that specific row.
print(df.loc["Bulbasaur":"Charmander"])#it returns a DataFrame containing the rows from "Bulbasaur" to "Charmander" (inclusive). The index of the returned DataFrame corresponds to the index labels of the original DataFrame, and all columns are included.
print(df.iloc[0])#it returns a Series containing the values of the first row of the DataFrame. The index of the Series corresponds to the column names of the DataFrame, and the values represent the data in that specific row.
print(df.iloc[0:5])#it returns a DataFrame containing the first 5 rows of the original DataFrame. The index of the returned DataFrame corresponds to the index of the original DataFrame, and all columns are included.
print(df.iloc[0:5,0:2])#it returns a DataFrame containing the first 5 rows and the first 2 columns of the original DataFrame. The index of the returned DataFrame corresponds to the index of the original DataFrame, and the columns represent the selected columns.