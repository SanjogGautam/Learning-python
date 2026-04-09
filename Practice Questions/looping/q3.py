'''3. WAP to input a number,
Find its reverse and then check whether it is palindrome or not.'''
n=int(input("Enter a number= "))
s=0
r=0
temp=n
while n!=0:
    r=n%10
    s=s*10+r
    n//=10
print("Reverse of the {} = {}".format(temp,s))
if s==temp:
    print("The number= {} is a palindrome".format(temp))
else:
    print("The number= {} is not a palindrome".format(temp))

