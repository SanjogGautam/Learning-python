import matplotlib.pyplot as plt
import numpy as np
names=["Sanjog","Swagat","Susan","Aswin"]
salary=np.array([40000,50000,45000,44000])
colors=["red","blue","green","orange"]
plt.pie(salary, labels=names, autopct="%1.1f%%", colors=colors, explode=[0,0.2,0,0], shadow=True,startangle=90)
plt.title("Salary Distribution")
# Use plt.text instead of annotate for pie charts to avoid coordinate madness
plt.text(1.069,-0.4, f"{names[1]} is Highest!", fontsize=12, fontweight='bold', color='blue')
plt.legend(title="Friends", loc=(1.069,0), shadow=True)
plt.show()
