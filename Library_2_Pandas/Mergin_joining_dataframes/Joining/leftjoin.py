import pandas as pd
employees= pd.DataFrame({
    "EmpID":[1,2,3,4],
    "Name":["Sanjog","Sarin","Swagat","Susan"],
    "DeptID":[10,20,10,30]
})
departments=pd.DataFrame({
    "DeptID":[10,20,40],
    "DeptName":["HR","Finance","IT"]
})
# Performing a left join
left=pd.merge(employees,departments,on="DeptID",how="left")
print(left)