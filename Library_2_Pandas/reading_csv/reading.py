import pandas as pd
df=pd.read_csv("data.csv")
print(df.head())
#we can specify sperator if it is not comma
#df=pd.read_csv("data.csv",sep=";")
#print(df)
