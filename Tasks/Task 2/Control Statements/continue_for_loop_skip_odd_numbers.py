#continue statement that skips the odd number in for loop
n=int(input('Enter the number= '))
for i in range(n+1):
    if i%2!=0:
        continue
    print(i)
