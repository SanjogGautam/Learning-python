#2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date
class person:
    def __init__(self,name,country,d_o_b):
        self.name=name
        self.country=country
        self.d_o_b=d_o_b
    def age(self):
        current_year=date.today().year
        return current_year-self.d_o_b
p1=person("Sanjog","Nepal",2005)
print(p1.age())
        
