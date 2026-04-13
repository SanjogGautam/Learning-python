# instead of manually opening and closing a file, we can use the with statement to automatically handle it for us
with open("Tasks/Task 5(File handling)/the with statement/b.txt", "wt") as file:
    file.write("My name is Sanjog Gautam\nI am a student of computer science")
with open("Tasks/Task 5(File handling)/the with statement/b.txt", "rt") as file:
    print(file.read())