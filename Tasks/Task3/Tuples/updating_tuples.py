#we can't change the value of tuple but can work around it by converting first to list and then back to tuple
tup1=(1,2,3,4,5)
y=list(tup1)
y[0]=10
tup1=tuple(y)
print (tup1)
#we can delete a tuple by using del tup1
