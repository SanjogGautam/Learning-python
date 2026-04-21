import pandas as pd
read = pd.read_csv("data.csv")
# print(read.columns)#it gives the column labels of the dataset
# print(read.index)#it gives the rows labels of the dataset
# print(read.dtypes)#it gives the data types of each column in the dataset
# print(read.size)#it gives the total number of elements in the dataset which is the product of the number of rows and columns in the dataset
# print(read.shape)#it gives the number of rows and columns in the dataset
# print(read.info())#it gives the summary of the dataset including the number of non-null values in each column and the data types of each column
# print(read.describe())#it gives the statistical summary of the dataset including the count, mean, standard deviation, minimum, and maximum values for each numerical column in the dataset
print(read.count())#it gives the number of non-null values in each column of the dataset