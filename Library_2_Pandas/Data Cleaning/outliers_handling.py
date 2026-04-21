import pandas as pd
df=pd.read_csv('data.csv',index_col="Name")
# 4. Handling outliers
# outliers can be handled by using the clip() method, which allows me to set a lower and upper bound for the values in a column.
# a. Clipping values to a specific range
df["Height"]=df["Height"].clip(lower=0, upper=3)#it clips the values in the "Height" column to a range of 0 to 3
print(df["Height"])
# b. Clipping values based on the mean and standard deviation
mean_height=df["Height"].mean()
std_height=df["Height"].std()
lower_bound=mean_height - 2*std_height
upper_bound=mean_height + 2*std_height
df["Height"]=df["Height"].clip(lower=lower_bound, upper=upper_bound)#it clips the values in the "Height" column to a range based on the mean and standard deviation
print(df["Height"])
# c. Removing outliers
df=df[(df["Height"]>=lower_bound) & (df["Height"]<=upper_bound)]#it removes all the rows that contain outliers in the "Height" column based on the mean and standard deviation
print(df["Height"])
# d. Handling outliers with the IQR method
Q1=df["Height"].quantile(0.25)#it calculates the first quartile of the "Height" column and stores it in a variable called "Q1"
Q3=df["Height"].quantile(0.75)#it calculates the third quartile of the "Height" column and stores it in a variable called "Q3"
IQR=Q3-Q1#it calculates the interquartile range of the "Height" column and stores it in a variable called "IQR"
lower_bound=Q1 - 1.5*IQR#it calculates the lower bound for the "Height" column based on the IQR
upper_bound=Q3 + 1.5*IQR#it calculates the upper bound for the "Height" column based on the IQR
df=df[(df["Height"]>=lower_bound) & (df["Height"]<=upper_bound)]#it removes all the rows that contain outliers in the "Height" column based on the IQR method
print(df["Height"])
