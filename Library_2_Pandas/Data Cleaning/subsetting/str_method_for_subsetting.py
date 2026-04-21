import pandas as pd
df=pd.read_csv("data.csv",index_col="Name")
print(df)
print(df["Type2"].str.contains("P"))
print(df["Type1"].str.startswith("W").to_string())
