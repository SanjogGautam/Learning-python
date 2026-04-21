with open("emp.csv", "r") as f:
    # Skip the header or use it for titles
    header = f.readline() 
    print(f"{'ID':<5} {'Name':<35} {'Address':<15} {'Salary':<10}")
    print("-" * 80)
    
    for line in f:
        # Remove the newline and split by comma
        data = line.strip().split(",")#strip removes white spaces from front and end and split is used to make the list out of the data wehere , is detected
        # Unpack the data into a formatted string
        print(f"{data[0]:<5} {data[1]:<35} {data[2]:<15} {data[3]:<10}")#:<30 gives 30 spaces in console
    