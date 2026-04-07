#continue statement in while loop that skips odd numbers
n=int(input("Enter the number= "))
i=0
while i<n+1:
    i+=1
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1
    
