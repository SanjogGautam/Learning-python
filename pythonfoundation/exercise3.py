'''Create a program that asks the user for three numbers and checks if
all of them are positive, or at least one of them is negative. Print the
result of the logical operation.
'''
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))

if n1>0 and n2>0 and n3>0:
    print("All the numbers are positive")
else:
    print("Atleast one number is negative")
