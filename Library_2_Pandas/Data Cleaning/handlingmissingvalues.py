import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")
#1. handling missing values
# missing values can be handled by either removing the rows or columns that contain them, or by filling them with a specific value such as the mean, median, or mode of the column.
# a.removing rows with missing values
cleaned_df=df.dropna(subset=["Type2"])#it removes all the rows that contain at least one missing value and creates a new dataframe called "cleaned_df"
print(cleaned_df)
# b. filling missing values with the mean
mean_value=df["Height"].mean()#it calculates the mean of the "Height" column and stores it in a variable called "mean_value"
full=df.fillna({"Type2":mean_value})#it fills the missing values in the "Type2" column with the mean value and creates a new dataframe called "full"
print(full)
# c. Dropping irrelevant columns
col=df.drop(columns=["Legendary","No"])#it drops the "Legendary" and "No" columns from the dataframe and creates a new dataframe called "col"
print(col)