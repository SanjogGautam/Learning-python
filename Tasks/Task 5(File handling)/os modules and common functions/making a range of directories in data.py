import os
if not os.path.exists("Tasks/Task 5(File handling)/os modules and common functions/data"):
    os.mkdir("Tasks/Task 5(File handling)/os modules and common functions/data")
for i in range(1, 11):
    os.mkdir(f"Tasks/Task 5(File handling)/os modules and common functions/data/dir_{i}")
