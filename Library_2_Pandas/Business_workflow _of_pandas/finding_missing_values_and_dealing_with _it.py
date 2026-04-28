import pandas as pd
df=pd.read_csv("bestsellers_with_categories.csv",index_col="Name")
print (df.head())
#finding for missing values
print (df.isnull().sum())
print(df.isnull().any())#to check if there is any missing value in the dataset
