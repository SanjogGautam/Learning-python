'''2. WAP to input two numbers, find their square root and then calculate their(square root) sum.'''
def sqrt(a):
    return a**0.5
    
n1=int(input("Enter the first number= "))
n2=int(input("Enter the second number= "))
sum = sqrt(n1)+sqrt(n2)
print(f"Squareroot of {n1}= {sqrt(n1)}")
print(f"Squareroot of {n2}= {sqrt(n2)}")
print(f"Sum of squareroot= {sum}")