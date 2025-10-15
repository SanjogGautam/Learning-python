emp=() #empty tuple
t1=(1,) #single element tuple
t2=(1,2,3,4,5)
t3=('a','b','c')
num=(1,2,'a','b',3.14)
a,*b,c=num #unpacking
print(a)
print(b)
print(c)
tuple1=(1,2,3)
del tuple1 #deleting entire tuple
#print(tuple1) #error
#built-in functions
num1=(1,2,2,2,2,3,4,5)
print(len(num1)) #length of tuple
print(min(num1)) #minimum element
print(max(num1)) #maximum element
print(sum(num1)) #sum of elements
print(num1.count(2)) #count of specific element

