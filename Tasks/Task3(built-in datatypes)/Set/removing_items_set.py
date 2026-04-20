#we can use remove or discard method to remove items in a set
#remove will throw error of the item is not in the list  but discard doesn't
a={"a","b","c","d"}
a.remove("a")
a.discard("a")
print(a)
#pop() randomly removes item for the set
a.pop()
print(a)
#clear() empties the entire set
a.clear()
print(a)
#del is used to delete the entirity of the given set
del a
print(a)
