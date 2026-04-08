a=[1,2,3,4]
b=a #it will create a reference to the list a and b will point to the same list in memory
print(a) #[1, 2, 3, 4]
print(b) #[1, 2, 3, 4]
a[0]=10 #it will change the first element of the list a to 10
print(a) #[10, 2, 3, 4]
print(b) #[10, 2, 3, 4] #it will also change the first element of the list b to 10 because a and b are pointing to the same list in memory
c=a.copy() #it will create a new list c which is a copy of the list a and c will point to a different list in memory
print(c) #[10, 2, 3, 4]
a[0]=20 #it will change the first element of the list a to 20
print(a) #[20, 2, 3, 4]
print(c) #[10, 2, 3, 4] #it will not change the first element of the list c because a and c are pointing to different lists in memory
