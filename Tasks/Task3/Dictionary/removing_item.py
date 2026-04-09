#we can remove item using the pop() function or del keyword.
a={
    'sanjog':'gautam',
    'age':20,
    'hobby':'coding',
    'country':'Nepal'}
#a.pop() function removes the item with the specified key and returns its value.
print(a.pop('age'))#it will remove the item with the key 'age' and return its value 20.
print(a)
#del keyword removes the item with the specified key.
del a['hobby']#it will remove the item with the key 'hobby'.
print(a)
