import matplotlib.pyplot as plt
import numpy as np
names_x=np.array(["Sanjog","Swagat","Susan","Aswin"])
income_y=np.array([40000,50000,45000,44000])
style=dict(
    color=["red","blue","green","orange"],
    edgecolor=["darkred","darkblue","darkgreen","darkorange"],
    linewidth=2,
    width=0.5
)
plt.bar(names_x,income_y,**style)
plt.xlabel("Friends Name")
plt.ylabel("Income")
plt.title("Income of Friends")
plt.annotate(f"{names_x[np.argmax(income_y)]} is the Highest Earner",xy=(np.argmax(income_y),income_y[np.argmax(income_y)]),xytext=(np.argmax(income_y)+0.2,income_y[np.argmax(income_y)]+1000),arrowprops=dict(color="black"))
plt.show()
#for getting horizontal chart we can use plt.barh()