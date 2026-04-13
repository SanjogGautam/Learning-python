#read()to read the content of the file. It reads the entire content of the file and returns it as a string.
file=open("Tasks/Task 5(File handling)/file reading and writing/a.txt", "rt")
print(file.read())# it reads the entire content of the file and returns it as a string.
file.close() 
#readline() to read the content of the file line by line. It reads one line at a time and returns it as a string.
file=open("Tasks/Task 5(File handling)/file reading and writing/a.txt", "rt")
print(file.readline()) # it reads one line at a time and returns it as a string.
print(file.readline()) # it reads the next line of the file and returns it as a string.
for i in file:
    print(i) # it reads the remaining lines of the file and returns it as a string.
file.close()# we can't use read method with readline method because it will read the entire content of the file and return it as a string. So we have to use readline method to read the content of the file line by line.
#seek() method is used to change the position of the file pointer. It takes one parameter: the number of bytes to move the file pointer. The default value is 0, which means the beginning of the file.
file=open("Tasks/Task 5(File handling)/file reading and writing/a.txt", "rt")
print(file.read()) # it reads the entire content of the file and returns it as a string.
file.seek(0) # it moves the file pointer to the beginning of the file.
print(file.read()) # it reads the entire content of the file and returns it as a string.
file.close()