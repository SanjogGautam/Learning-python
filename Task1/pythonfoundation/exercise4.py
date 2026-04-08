'''Create a program that asks the user for three numbers and check for
each number if it divisible by 3, 4, or 7. Print the result each time'''
n1=int(input("Enter First number: "))
n2=int(input("Enter Second number: "))
n3=int(input("Enter Third number: "))
numbers=[n1,n2,n3]
for n in numbers:
    for i in [3,4,7]:
        if n%i==0:
            div= n/i
            print(div)
    
