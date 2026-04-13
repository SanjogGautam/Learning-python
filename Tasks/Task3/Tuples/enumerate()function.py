#enumerate() adds a counter as a key of enumerate object
#meaning it basically adds a conter to the given set
x=("a","b")
y=enumerate(x)
print(y)#it gives the location of the enumerate object
print(list(y))#it gives the count of the tuple x like((0,"a"),(1,"b"))
print(list(enumerate(x,1)))#it gives the count of the tuple x starting from 1 like((1,"a"),(2,"b"))
list1=["a","b"]
print(list(enumerate(list1)))#it gives the count of the list list1 like((0,"a"),(1,"b"))
print(list(enumerate(list1,1)))#it gives the count of the list list1 starting from 1 like((1,"a"),(2,"b"))