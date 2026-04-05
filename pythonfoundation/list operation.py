#list
x=[1,123,5,12,3]
#list slicing
print(x[0:2])
#nested list
x=[[1,35,2],123,3,5]
print(x[0][1])
#lenght of a string
print(len(x))
#replication of a string
x=[1,2,3]
print(x*3)
#element deletion
x=[1,2,3,4]
del(x[2])
print(x)
#using of in and not in it gives boolean true or false
x=[1,2,3,4]
y=1 in x
print(y)
#use of index fuction
x=[1,2,3,4]
print(x.index(1))
#insering
x=[1,2,3,4]
x.insert(2,5)
print(x)
#sorting
x=[123,21,1,5]
x.sort()
print(x)
