import pandas as pd
df=pd.read_csv("data.csv",na_values=["N/A","NA","missing","-"," "])
print(df.to_string())