#f string is the preffered way of string formatting in python 
#to use f string we need to prefix the string with f or F and then we can use curly braces {} to insert the values of variables or expressions inside the string
#{} are placeholders
#: is used as modifier to specify the format of the value inside the placeholder
name="Sanjog"
age=25
print(f"My name is {name} and I am {age} years old.")#using f string to format the string
#we can also use expressions inside the placeholders
print(f"My name is {name.upper()} and I am {age+5} years old.")
print(f"My name is {name.lower()} and I am {age-5} years old.")
print(f"The price is {100:.2f} dollars.")