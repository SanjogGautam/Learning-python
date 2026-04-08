'''4. Write a program that prints the first n even numbers. Ask the user for
the value of n. Use a for loop to generate the numbers, and an if
statement to determine if the current number is even.'''
n= int(input("Enter the number= "))
for i in range(1,n+1):
    if i%2==0:
        print(i)
if n%2==0:
    print(f"The current number{n} is even")
    
    
