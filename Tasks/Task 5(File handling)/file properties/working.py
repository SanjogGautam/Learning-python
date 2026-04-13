file= open("Tasks/Task 5(File handling)/file properties/c.txt", "w")
print(file.name) # prints the name of the file
print(file.closed) # checks if the file is closed or not
print(file.mode) # prints the mode in which the file is opened
file.close() # closing the file
print(file.closed) # checks if the file is closed or not