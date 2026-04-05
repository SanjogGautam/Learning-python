'''Write a program that asks the user to input two numbers and then
performs both a modulus and floor division operation on those
numbers. Print the results of both operations to the screen.
'''
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
#modulus operation
mod=n1%n2
print(f"Remainder= {mod}")
#floor division
floordiv = n1//n2
print(f"Floor Division= {floordiv}")
