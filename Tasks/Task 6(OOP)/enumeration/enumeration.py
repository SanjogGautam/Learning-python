#In Python, Enumeration (or Enum) is a way to create a set of symbolic names (members) bound to unique, constant values.
from enum import Enum

# Define your choices
class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


my_choice = Level.HARD
print(my_choice)
print(my_choice.name)
print(my_choice.value)
if my_choice == Level.HARD:
    print("Be careful! This is the HARD mode.")
for i in Level:
    print(i.name,i.value)