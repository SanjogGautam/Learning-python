#Set operations in Python
set1={1,2,3,4,5}
set2={4,5,6,7,8}
#Union of two sets
union=set1.union(set2)
print(union)
set3=set1|set2#it can't union the set1 and set2 because it is not a valid operator for sets but we can use the union method to get the union of two sets
print(set3)
set1.update(set2)#it will update the set1 with the elements of set2 and return 
print(set1)
#Intersection of two sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
intersection=set1.intersection(set2)
print(intersection)
set3=set1&set2#it can't intersect the set1 and set2 because it is not a valid operator for sets but we can use the intersection method to get the intersection of two sets
print(set3)
set1.intersection_update(set2)#it will update the set1 with the elements of set2 
print(set1)
#Difference of two sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
difference=set1.difference(set2)
print(difference)
set3=set1-set2#it can't difference the set1 and set2 because it is not a valid operator for sets but we can use the difference method to get the difference of two sets
print(set3)
set1.difference_update(set2)#it will update the set1 with the elements of set2
print(set1)
#Symmetric difference of two sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
sym_diff=set1.symmetric_difference(set2)
print(sym_diff)
set3=set1^set2#it can't symmetric difference the set1 and set2 because it is not a valid operator for sets but we can use the symmetric_difference method to get the symmetric difference of two sets
print(set3)
set1.symmetric_difference_update(set2)#it will update the set1 with the elements of set2 
print(set1)