'''2. Create a function that takes a string as a parameter, and returns the
number of vowels in the string.'''
s=input("ennter the string: ")

def v(ss):
    vowels='aeiou'
    count=0
    for i in ss:
        if i in vowels:
            count=count+1
    return count
result= v(s)
print(f"Total vowels in {s} is {result}")
