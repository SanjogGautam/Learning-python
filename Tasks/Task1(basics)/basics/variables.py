x=100  #integer
print(type(x))
print(x)
#float
x=3.14
print(type(x))
print(x)
#string
x="hello"
print(type(x))
print(x)
#list
x=[14,15,16]
print(type(x))
print(x)
print(x[0])
x[1]=144
print(x)
#tuple
x=(1,2,3,4)
print(type(x))
print(x)
# we can't change the value of tuple imutable x[0]=100
#print(x)
x='sanjog gautam'
print(type(x))
print(x)
print(x[0])
#file pointers
x=open('variables.txt','w')
print(type(x))
(x,y,z)=(10,20,30)
print(x)
print(y)
print(z)
x=y=z=100
print(x,y,z)