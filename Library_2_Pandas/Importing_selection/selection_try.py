import pandas as pd
df=pd.read_csv("data.csv",index_col="Name")
name=input("Enter the name of the pokemon: ")
try: 
    print(df.loc[name])
except Exception as e:
    print("The pokemon name you entered is not in the dataframe. Please check the spelling and try again.")