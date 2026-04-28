import pandas as pd
df=pd.read_csv("bestsellers_with_categories.csv",index_col="Name")
#"Which category is performing best?"
df.groupby("User Rating")
