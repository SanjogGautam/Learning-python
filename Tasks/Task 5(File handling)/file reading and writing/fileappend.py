#a doesn't overwrite the file but adds to it
file=open("Tasks/Task 5(File handling)/file reading and writing/a.txt", "at") #at means append text mode which is used to open a file for appending. If the file does not exist, it will be created.
file.write("I am currently living in Kirtipur. \nMy Father name is Bhim Gautam") #write() method is used to write data to the file.
file.close()
file=open("Tasks/Task 5(File handling)/file reading and writing/a.txt", "rt")
print(file.read())
file.close()