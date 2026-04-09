#enumerate() adds a counter as a key of enumerate object
#meaning it basically adds a conter to the given set
x=("a","b")
y=enumerate(x)
print(y)#it gives the location of the enumerate object
print(list(y))#it gives the count of the tuple x like((0,"a"),(1,"b"))
