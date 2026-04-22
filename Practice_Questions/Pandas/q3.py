#5. Read from "emp.csv" and display records of only those whose salary is more than 35000.
import pandas as pd
read=pd.read_csv("emp.csv")
print(read[read["salary"]>35000])