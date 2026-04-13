file=open("Tasks/Task 5(File handling)/file reading and writing/b.txt", "wt")
file.write("This is a new line. \nMy name is Sanjog Gautam") # it creates a new file as the file b.txt doesn't exit
file.close()
file=open("Tasks/Task 5(File handling)/file reading and writing/b.txt", "rt")
print(file.read())
file.close()
file=open("Tasks/Task 5(File handling)/file reading and writing/b.txt", "wt") 
file.write("My name is Mogamboo. \nI am a super villain.") # it overwrites the content of the file as the file b.txt already exists
file.close()
file=open("Tasks/Task 5(File handling)/file reading and writing/b.txt", "rt")
print(file.read())