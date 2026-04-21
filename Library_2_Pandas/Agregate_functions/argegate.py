import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")
group=df.groupby("Type1")#it groups the dataframe by the "Type1" column and creates a groupby object
print(df.mean(numeric_only=True))#it calculates the mean of the numeric columns for each group and prints the result
print(df.count())#it counts the number of non-null values in each column for each group and prints the result
print(group["Height"].max(numeric_only=True))#it calculates the maximum value of the "Attack" column for each group and prints the result
