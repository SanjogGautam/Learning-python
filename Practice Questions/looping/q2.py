'''2. WAP to input a number and print all of its digits.
Also find the sum of all digits.'''
n=int(input("Enter a number= "))
sum=0
temp=0
digits_list=[]
while n!=0:
    temp=n%10
    digits_list.append(temp)
    sum+=temp
    n//=10

for i in reversed(digits_list):#reversed()will sort the list in reverse order
    print(i)
print("sum of all the digits= {}".format(sum))
