'''Create a program that asks the user for two numbers and checks if the
first number is equal to, greater than, or less than the second number.
Print the results of each comparison.'''

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1==num2:
    print("The numbers are equal")
elif num1>num2:
    print("Num1 is greater")
else:
    print("Num2 is greater")
