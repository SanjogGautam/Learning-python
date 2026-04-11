'''WAP to input a sentence and count the frequency of all characters.'''
sent=input("Enter a sentence= ")
count={}
for i in sent:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i,j in count.items():
    print(i," = ",j)
