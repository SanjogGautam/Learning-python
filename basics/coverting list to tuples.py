num=[1,2,3,4,5]
tup= tuple(num) #converting list to tuple
print(tup)
#we can't change tuple after creation

#nesting tuples in list
lst=[(1,2),(3,4),(5,6)]
print(lst)
lst.append((7,8)) #adding new tuple to list
print(lst)
lst.remove((3,4)) #removing tuple from list
print(lst)
#we can change list after creation

#nesting list in tuple
tup1=([1,2],[3,4],[5,6])
print(tup1)
tup1[0].append(3) #adding element to list inside tuple
print(tup1)
tup1[1].remove(4) #removing element from list inside tuple
print(tup1)
#we can't change tuple after creation but we can change list inside tuple