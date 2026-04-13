#lambda function with built-in functions like map(), filter() and sorted()
#map() functions apllies a its method to every item in a iterable
numbers=[1,2,3,4,5]
double=list(map(lambda x: x*2, numbers))
print(double)
# filter()- it creates a list of items for which a funcitn returns True
numbers=[1,2,3,4,5]
odd=list(filter(lambda x: x%2!=0,numbers))
print(odd)
#sorted()-it is used to sort a custom dataformat
sanjog=[("Sanjog",20),("Sarin",21),("Helish",22)]
new=sroted(sanjog,key= lambda x: len(x))#IT sorts according to the length of the string

