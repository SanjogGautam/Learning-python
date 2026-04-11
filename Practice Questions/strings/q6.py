'''WAP to input name of 5 countries and print only those which start with "N".'''
names=[]
for i in range(1,6):
    name=input(f"{i} Enter your country name=" )
    names.append(name)
for i in names:
    if i[0].upper()=="N":
        print(i)
