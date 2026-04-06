# Avoid using 'list' as a variable name because it is a built-in Python function
fruits = ["apples", "banana", "mango", "guava", "peach"]

fruit = input("Enter the name of the fruit: ")

if fruit in fruits:
    print("The fruit is in the list") # Only 4 spaces (or 1 tab) here
else:
    print("The fruit is not in the list")
