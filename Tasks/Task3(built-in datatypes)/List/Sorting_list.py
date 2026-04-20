# List sorting
a=[10,13,5,2,1]
a.sort()
print(a)#sorts in ascending order
a.sort(reverse=True)#sorts in descending order
print(a)
a=[10,13,5,2,1]
a.reverse()#sorts in reverse order
print(a)
b=["sanjog","helish","Swagat"]
b.sort(key = str.lower)#key=str.lower(sort is case sensitive to make it insensitive we do this)
print(b)


