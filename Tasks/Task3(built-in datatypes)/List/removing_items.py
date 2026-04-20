l=["Sanjog","Helish","Sarin"]
l.remove("Sanjog") #it will remove the specified element from the list
print(l) 
l.pop(1) #it will remove the element at the specified index and return it
print(l)
l.pop() #it will remove the last element from the list and return it
print(l)
l=["Sanjog","Helish","Sarin"]
del l[0] #it will remove the element at the specified index
print(l)
del l #it will delete the entire list
#print(l) it will give an error because the list is deleted
l.clear() #it will remove all the elements from the list but the list will still exist
print(l) #[] it will print an empty list because all the elements are removed from the list