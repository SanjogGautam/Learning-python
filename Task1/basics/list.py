num=[1,2,3,4,5]
print(num)
letter=['a','b','c','d']
print(letter)
stg=['sanjog',123,3.14,'gautam']
print(stg)
mat=[[1,2,3],['a','b'],[7,8,9]]
print(mat)
print(stg[2])
mix=[1,2,'a','b',3.14]
print(mix[1:4]) #slicing
print(mix[::2]) #slicing with step
print(mix[::-1]) #reverse order print

#operations on list
z=[0]*10
print(z)
a=[1,2,3]
b=['a','b','c']
print(a+b) #concatenation
var=list('sanjog') 
print(var)
one,*other=num #unpacking
print(one)
print(other)

#list methods
num.append(6) #add element at the end
print(num)
num.extend([7,8,9]) #add multiple elements at the end
print(num)
num.insert(0,0) #add element at specific index
print(num)
num.remove(3) #remove specific element
print(num)
var1=['d','a','c','b']
var1.sort() #sort the list
print(var1)
x=[3,1,4,2]
print(len(x)) #length of list
print(min(x)) #minimum element
print(max(x)) #maximum element
print(sum(x)) #sum of elements
print(sum(x)/len(x)) #average of elements
