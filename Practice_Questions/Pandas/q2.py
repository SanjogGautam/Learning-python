#4. Read from "emp.csv" and display all records.
import pandas as pd
read=pd.read_csv("emp.csv")
print(read.to_string())
print(read.info())
