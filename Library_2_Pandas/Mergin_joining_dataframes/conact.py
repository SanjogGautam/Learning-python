#concat() method is used to concatenate two or more dataframes along a particular axis (rows or columns).
# a. Concatenating dataframes along rows
import pandas as pd
df1=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
df2=pd.DataFrame({"A":[7,8,9],"B":[10,11,12]})
concatenated_df=pd.concat([df1,df2],axis=0,ignore_index=True)#it concatenates the two dataframes along rows and creates a new dataframe called "concatenated_df"
print(concatenated_df)
# b. Concatenating dataframes along columns
df3=pd.DataFrame({"C":[13,14,15]})
concatenated_df2=pd.concat([df1,df3],axis=1)#it concatenates the two dataframes along columns and creates a new dataframe called "concatenated_df2"
print(concatenated_df2)
# c. Concatenating dataframes with different indexes
df4=pd.DataFrame({"A":[16,17,18],"B":[19,20,21]},index=[3,4,5])
concatenated_df3=pd.concat([df1,df4],axis=0)#it concatenates the two dataframes along rows and creates a new dataframe called "concatenated_df3" with different indexes
print(concatenated_df3)
# d. Concatenating dataframes with different columns
df5=pd.DataFrame({"D":[22,23,24]})
concatenated_df4=pd.concat([df1,df5],axis=1)#it concatenates the two dataframes along columns and creates a new dataframe called "concatenated_df4" with different columns
print(concatenated_df4)

