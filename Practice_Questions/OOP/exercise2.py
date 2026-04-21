'''2. Create a class called Student that inherits from Person. The class
must have a constructor that takes in the name, age, occupation, and a
list of subjects. The class should have a method get_subjects() that
returns the list of subjects. Create an instance of the class and call the
methods to display the values.'''

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

class Student(Person):
    # 1. The child __init__ must take ALL the arguments
    def __init__(self, name, age, occupation, subjects):
        # 2. super() goes INSIDE the __init__
        super().__init__(name, age, occupation)
        self.subjects = subjects

    def get_subjects(self):
        return self.subjects

# 3. Pass the subjects as a list as requested
s1 = Student("Sanjog", 20, "Bachelor's Student", ["Web Security", "Python", "RPA"])



print(f"Name: {s1.get_name()}")
print(f"Age: {s1.get_age()}")
print(f"Occupation: {s1.get_occupation()}")
print(f"Subjects: {', '.join(s1.get_subjects())}") # Using .join() like we practiced!
