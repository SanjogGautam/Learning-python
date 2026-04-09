'''4. WAP to print all prime numbers from a to b where and a and b are
taken as input from user.'''
a=int(input("Enter the value of a= "))
b=int(input("Enter the value of b= "))
for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count==2:
        print(i)
    
    
