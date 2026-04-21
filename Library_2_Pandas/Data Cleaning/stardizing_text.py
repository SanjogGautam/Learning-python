# 5. standardize text
import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")
# standardizing text can be done by using the str.lower() method, which converts all the characters in a string to lowercase.
# a. Standardizing text to lowercasea
df["Type1"]=df["Type1"].str.lower()#it converts all the characters in the "Type1" column to lowercase
print(df["Type1"])
# b. Standardizing text to uppercase
df["Type2"]=df["Type2"].str.upper()#it converts all the characters in the "Type2" column to uppercase
print(df["Type2"])
# c. Standardizing text to title case
df["Type1"]=df["Type1"].str.title()#it converts all the characters in the "Type1" column to title case// first letter of each word is capitalized and the rest are lowercase
print(df["Type1"])