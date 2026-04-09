#Frozen Set
#it is a imutable version of a given set and created using frozenset()
x=frozenset({"a","b","c"})
print(x)
print(type(x))
x.pop()#this will throw an error
print(x)
