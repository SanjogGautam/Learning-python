import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")#it reads the csv file and sets the "Name" column as the index of the dataframe
#print(df.to_string())#it prints the entire dataframe without truncating any part of it
#to access a specific column data
print(df["Weight"])#it accesses the "Weight" column of the dataframe and prints it
#to access a specific row data
print(df.loc["Pikachu"])#it accesses the row with index "Pikachu" and prints it
print(df.iloc[0])#it accesses the first row of the dataframe and prints it
#to access multiple columns data
print(df[["Weight","Height"]])#it accesses the "Weight" and "Height" columns of the dataframe and prints them
#to access multiple rows data
print(df.loc[["Pikachu","Bulbasaur"]])#it accesses the rows with index "Pikachu" and "Bulbasaur" and prints them
print(df.iloc[[0,1]])#it accesses the first and second rows of the dataframe
#to access a specific element in the dataframe
print(df.loc["Pikachu","Weight"])#it accesses the element in the row with index "Pikachu" and column "Weight" and prints it
print(df.iloc[0,0])#it accesses the element in the first row and first column of the dataframe and prints it
#to access a range of rows and columns
print(df.loc["Pikachu":"Bulbasaur","Weight":"Height"])#it accesses the range of rows from "Pikachu" to "Bulbasaur" and columns from "Weight" to "Height" and prints them
print(df.iloc[0:2,0:2])#it accesses the range of rows from index 0 to 1 and columns from index 0 to 1 and prints them