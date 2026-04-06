'''1. Create a class called Person with a constructor that takes in the
person's name, age and occupation. The class should have methods
get_name(), get_age() and get_occupation() that return the respective
values. Create an instance of the class and call the methods to display
the values.'''
class person:
    def __init__(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_occupation(self):
        return self.occupation
p1=person("sanjog",20,"IT student")
print(f"The name of the person={p1.get_name()}\nThe age of the person={p1.get_age()}\nThe occupation of the person={p1.get_occupation()}\n")
