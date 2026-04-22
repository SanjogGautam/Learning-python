#3. Create a csv file "emp.csv" to store id, name, address, salary of 5 employees.
import pandas as pd
df=pd.DataFrame({
    "name":["Sanjog","Sarin","Swagat","Susan","Bibek"],
    "address":["Parbat","Kirtipur","Nuwakot","Dang","Bajang"],
    "salary":[40000,49000,60000,80000,100000]
})
df.to_csv("emp.csv",index=False)