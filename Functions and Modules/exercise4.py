'''4. Create a function that takes a number as a parameter, and returns a
message indicating if the number is positive, negative or zero.'''
n=int(input("Enter the number: "))
def check(num):
    if(num==0):
        print("The number is zero: ")
    elif num>0:
        print("The number is positive")
    else:
        print("The number is negative")
check(n)
