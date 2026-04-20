#5. Read from "emp.csv" and display records of only those whose salary is more than 35000.
with open("emp.csv","r") as f:
    header=f.readline()
    print("-"*10,"List of Employess salary >35000","-"*10)
    print(f"{'ID':>5} {'Name':>20} {'Address':>20} {'Salary':>10}")
    print("-"*70)
    for line in f:#for reading new line 
        data=line.strip().split(",")
        if(int(data[3])>35000):
            print(f"{data[0]:>5} {data[1]:>20} {data[2]:>20} {data[3]:>10}")


