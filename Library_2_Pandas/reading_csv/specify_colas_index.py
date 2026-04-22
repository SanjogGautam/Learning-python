import pandas as pd
read=pd.read_csv("data.csv",index_col="Name")#specifying index column while reading csv file
print(read)