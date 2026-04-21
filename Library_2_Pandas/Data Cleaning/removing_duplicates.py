import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")
# 2. Removing duplicates
# duplicates can be removed by using the drop_duplicates() method, which removes all duplicate rows from the dataframe.
# a. Removing duplicate rows
unique_df=df.drop_duplicates()#it removes all duplicate rows from the dataframe and creates a new dataframe called "unique_df"
print(unique_df)
# b. Removing duplicate rows based on a specific column
unique_df_by_type=df.drop_duplicates(subset=["Type2"])#it removes all duplicate rows based on the "Type2" column and creates a new dataframe called "unique_df_by_type"
print(unique_df_by_type)
# fixing inconsistent values
df["Type2"]=df["Type2"].replace({"None":"Nan"})#it replaces all the occurrences of the string "None" in the "Type2" column with the pandas NA value
print(df["Type2"])