#looping in tuple is same as looping in list it is very simple and is done using for and while loops
x=(1,2,3,4)
for i in x:
    print(i)
#but in while we need indexing
i=0
while i<(len(x)):
    print(x[i])
    i+=1
