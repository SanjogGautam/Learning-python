'''4. WAP to input 3 different numbers and print the middle number.'''
def middle_num(a,b,c):
    if (a>=b and a<=c) or (a>=c and a<=b):
        return a
    elif (b>=a and b<=c) or (b>=c and b<=a):
        return b
    else:
        return c
n1=int(input("Enter the first number= "))
n2=int(input("Enter the second number= "))
n3=int(input("Enter the third number= "))
print(f"The middle number among {n1},{n2},{n3}={middle_num(n1,n2,n3)}")