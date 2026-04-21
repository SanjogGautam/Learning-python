#3. Create a csv file "emp.csv" to store id, name, address, salary of 5 employees.
emp_id, emp_name, emp_address, emp_salary = [], [], [], []
print("Enter the data of the employees")
for i in range(5):
    print(f"{i+1} Employee id= ",end=""),emp_id.append(int(input()))
    print(f"{i+1} Employee Name= ",end=""),emp_name.append(input())
    print(f"{i+1} Employee Address= ",end=""),emp_address.append(input())
    print(f"{i+1} Employee Salary= ",end=""),emp_salary.append(int(input()))
with open("emp.csv","w") as f:
    f.write("Id,Name,Address,Salary\n")#adding a header line so that excel/pandas knows what the columns are
    for i in range(5):
        row=f"{emp_id[i]},{emp_name[i]},{emp_address[i]},{emp_salary[i]}\n"
        f.write(row)
