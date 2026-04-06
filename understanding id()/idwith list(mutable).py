a=[1,2,3]
b=a# refers to same object as a
c=[1,2,3]# a new object with same value as a
print(id(a)==id(b))# True
print(id(a)==id(c))# False

lst=[1,2,3]
print(id(lst))# id of lst
lst.append(4)#modifying the object
print(id(lst))# id remains same after modification because list is mutable
