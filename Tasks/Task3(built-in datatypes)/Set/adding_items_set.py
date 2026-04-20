#adding or removing items
#add() to add a single element in a set
set1={1,2,3}
set1.add(1)
print(set1)
#update() to add items from another set to the current set(it can be list, tuple anything)
l=["a","b"]
set1.update(l)
print(set1)
#update changes the entire set it is currently working on
