'''2. Create a function that takes a list of 5 country
names and then return only those countries that start with 'N'.'''
def names_N(names):
    result=[]
    for i in names:
        if i[0] in "Nn":
            result.append(i)
    return result
names_countries=[]
for i in range(0,5):
    name=input(f"{i+1} country= ")
    names_countries.append(name)
print(names_N(names_countries))
    
