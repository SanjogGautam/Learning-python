x="sanjog"
f=x.strip("sa")#it will remove jog from sanjog
print(f)
x="sanjog"
y=x.rstrip("san") 
print(y)
z= x.replace("san","")#it will replace san with an empty string in sanjog
print(z)
a=x.split("n")#it will split the string sanjog into two parts sa and jog and returs a list
print(a)
a="!".join(x)#it will join the characters of sanjog with ! in between and return a string
print(a)