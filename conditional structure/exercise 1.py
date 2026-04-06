'''Write a program that asks the user for an integer and calculates the
factorial of the given number. Use a for loop to accomplish this task.'''
num = int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact= fact *i
print (f"The factorial of {num} = {fact}")
