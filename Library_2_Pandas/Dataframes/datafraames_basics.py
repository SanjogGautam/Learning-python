#a dataframe is a tabular data structure with rows and columns similar to a excell spreadsheet
#its in 2D
#it is like a excell spreadsheet
import pandas as pd
data={
    "Name":["Sanjog","Sarin","Swagat","Susan"],
    "Age":[20,21,21,22]
}
#by default the indexing starts from 0 but we can also specify the indexes
df=pd.DataFrame(data,index=["Student1","Student2","Student3","Student4"])
print(df)
#to access a specific row data
print(df.iloc[0])
print(df.loc["Student3"])
#adding a new column
df["Address"]=["Parbat","Kirtipur","Nuwakot","Dang"]
print(df)
#adding a new row
newrows=pd.DataFrame({"Name":["Bibek","Kushal"],
                       "Age":[22,21],
                       "Address":["Bajang","Dhanding"]},index=["Student5","Student6"])
df=pd.concat([df,newrows])
print(df)
#accessing elements in a dataset
print(df.loc[:,"Age"])
print(df.iloc[1])#access row 1
print(df.iloc[1,0])#accessing sarins name[row,column]
print(df.iloc[::-1])#print in reverse order


