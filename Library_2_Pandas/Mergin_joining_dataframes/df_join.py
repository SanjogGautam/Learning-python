#df.join(df2) # Join two DataFrames on their indexes.
#.join() method is used to join two dataframes based on their indexes. It is a convenient method for combining dataframes when the indexes are the same or when you want to join on the index.
import pandas as pd
# Creating two dataframes
df1=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]},index=["a","b","c"])
df2=pd.DataFrame({"C":[7,8,9],"D":[10,11,12]},index=["a","b","c"])
print ("DataFrame 1:")
print(df1)
print ("DataFrame 2:")
print(df2)  
# Joining the dataframes using join() method
joined_df=df1.join(df2)#it joins the two dataframes based on their indexes and creates a new dataframe called "joined_df"
print(joined_df)