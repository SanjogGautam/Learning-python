import pandas as pd
read=pd.read_csv("data.csv",header=None,names=["Column1","Column2","Column3","Column4"])#specifying header as None and providing column names
print(read)