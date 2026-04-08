a=[1,2,3]
b=["Sanjog","Sarin","Helish"]
c=a+b #it will join the two lists and create a new list
print(c) #[1, 2, 3, 'Sanjog', 'Sarin', 'Helish']
c=[i for i in a] + [i for i in b] #it will join the two lists and create a new list using list comprehension
print(c) #[1, 2, 3, 'Sanjog', 'Sarin', 'Helish']
a.extend(c)
print(a) #[1, 2, 3, 1, 2, 3, 'Sanjog', 'Sarin', 'Helish']