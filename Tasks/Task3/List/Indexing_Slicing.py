a=["Sanjog","Sarin","Helish"]
#indexing
print(a[0]) #Sanjog
print(a[1]) #Sarin
print(a[2]) #Helish
print(a[-1]) #Helish
print(a[-2]) #Sarin
print(a[-3]) #Sanjog
#slicing
print(a[0:2]) #['Sanjog', 'Sarin']
print(a[1:3]) #['Sarin', 'Helish']
print(a[:2]) #['Sanjog', 'Sarin']
print(a[1:]) #['Sarin', 'Helish']
print(a[:]) #['Sanjog', 'Sarin', 'Helish']
print(a[::2]) #['Sanjog', 'Helish']#it takes every element with step of 2 but in list it will take first and third element
print(a[::-1]) #['Helish', 'Sarin', 'Sanjog']#it will reverse the list
print(a[-1::-1]) #['Helish', 'Sarin', 'Sanjog']#it will reverse the list using negative indexing
