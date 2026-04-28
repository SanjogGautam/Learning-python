import pandas as pd
df=pd.read_csv('bestsellers_with_categories.csv')
#df.drop_duplicates() to remove double entries. By default, it considers all the columns to identify duplicates. If you want to consider specific columns, you can use the subset parameter. For example, df.drop_duplicates(subset=['Name', 'Author']) will remove duplicates based on the 'Name' and 'Author' columns.
#By default, it keeps the first occurrence of the duplicate and removes the rest. If you want to keep the last occurrence, you can use the keep parameter. For example, df.drop_duplicates(keep='last') will keep the last occurrence of the duplicate and remove the rest.
#If you want to remove all duplicates and keep only unique rows, you can set the keep parameter to False. For example, df.drop_duplicates(keep=False) will remove all duplicates and keep only unique rows.
print(df.drop_duplicates())#remove duplicates and print the resulting DataFrame
df.to_csv('bestsellers_with_categories_no_duplicates.csv', index=False)#save the resulting DataFrame to a new CSV file without the index column