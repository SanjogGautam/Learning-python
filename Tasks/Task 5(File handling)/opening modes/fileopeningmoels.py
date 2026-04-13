#open() function is used to open a file while creatin a file object. It takes two parameters: the name of the file and the mode in which the file is opened. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'x' for creating a new file.

#file = open("Tasks/Task 5(File handling)/opening modes/a.txt", "xt") #xt means create text mode which is used to create a new file and open it for writing. If the file already exists, it will raise a FileExistsError.
file=open("Tasks/Task 5(File handling)/opening modes/a.txt", "wt") #wt means write text mode which is used to open a file for writing. If the file does not exist, it will be created.
file.write("This is a new line. \nMy name is Sanjog Gautam") #write() method is used to write data to the file.
file.close()
file=open("Tasks/Task 5(File handling)/opening modes/a.txt", "rt") 
print(file.read())
file.close() #close() method is used to close the file.
'''
r= reading
w= writing
a= appending
x= creating a new file
t= text mode
b= binary mode
default mode is text mode and reading mode. If the file does not exist, it will raise a FileNotFoundError.
'''