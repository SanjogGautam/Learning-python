import os
os.rmdir("Tasks/Task 5(File handling)/os modules and common functions/data/Day_10")
#it deletes the directory. It can only delete empty directories. If the directory is not empty it raises an error.
os.removedirs("Tasks/Task 5(File handling)/os modules and common functions/data/Day_9")
#it deletes the directory and all the intermediate directories. It can delete non empty directories. If the directory is not empty it deletes all the files and subdirectories in it and then deletes the directory.
os.remove("Tasks/Task 5(File handling)/os modules and common functions/data/Day_8/file.txt")
#it deletes the file. It can only delete files. If the file does not exist it raises an error. If the path is a directory it raises an error.
