'''WAP to input name of 5 countries and sort them in ascending order and
also in descending order.'''
names=[]
for i in range(5):
    name=input(f"{i+1} Enter the name= ")
    names.append(name)
names.sort(key=str.lower)
print(names)
names.sort(reverse=True,key=str.lower)
print(names)
