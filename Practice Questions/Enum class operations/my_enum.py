# i have to perform enum class opertions 

from enum import Enum,unique
@unique#this prevents two string to have same integer value 
class status(Enum):
    TODO=1
    DOING=2
    DONE=3
    ARCHIVED=4
    #HELLO=1 this throws an error 

#Operations done 
#accessing names and values
current=status.DOING
print(current)
print(current.name)
print(current.value)
#since enums are iterables we can loop through it using loops
for i in status:
    print(i.name)
#membership
if status.DONE in status:
    print("DONE is a valid status")
#is equal
my_status=status.DOING
if my_status is status.DOING:
    print("Task is ongoing")
#conversion of string and integer value to enum
sanjog=status(3)
print(sanjog)#status.DONE
gautam=status['DOING']
print(gautam)#status.DOING
