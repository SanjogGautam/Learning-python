import pandas as pd
data=pd.read_csv("data.csv",index_col="Name")
print(data)
print(data.query("Height>=2"))