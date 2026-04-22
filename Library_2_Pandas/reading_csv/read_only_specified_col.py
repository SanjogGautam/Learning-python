import pandas as pd
read=pd.read_csv("data.csv",usecols=["Name","Height"])
print(read)
#skiping rows
read=pd.read_csv("data.csv",skiprows=4)
print(read)
