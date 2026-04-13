import os
folders= os.listdir("Tasks/Task 5(File handling)/os modules and common functions/data")
print(folders)
for i in folders:
    print(i)
    print(os.listdir(f"Tasks/Task 5(File handling)/os modules and common functions/data/{i}"))
    #it lists the files in the directories. Since there are no files in the directories it returns empty list.
