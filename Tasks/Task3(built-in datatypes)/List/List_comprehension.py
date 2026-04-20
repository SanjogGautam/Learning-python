# List Comprehension
a=["sanjog","sarin","helish","sarbajeet"]
a1=[x for x in a]
print(a1)
a2=[x for x in a if "a" in x ]#printing those who has a in name
print(a2)
a3=[x for x in range(4)]
print(a3)
a4=[x for x in range(10) if x%2==0]#even no list
print(a4)
a5=["hello" for x in a]#replaces everything with hello in list a for a5
print(a5)