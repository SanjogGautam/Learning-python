'''3. Create a function that takes two strings as parameters and returns a
message indicating if both strings are equal or not.
'''
def comparestring(string1, string2):
    if(string1==string2):
        print("The strings are euqal")
    else:
        print("The strings are not equal")

s1=input("Enter the first string: ")
s2= input("Enter the second string: ")
comparestring(s1,s2)
