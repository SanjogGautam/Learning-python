import matplotlib.pyplot as plt
import numpy as np
names_x=np.array(["Sanjog","Swagat","Susan","Aswin"])
income_y=np.array([40000,50000,45000,44000])
style=dict(
    marker="o",
    markersize=10,
    markerfacecolor="red",
    markeredgecolor="red",
    linestyle="dashed",
    color="green"
)
plt.plot(names_x,income_y,**style)
plt.xticks(names_x)
plt.xlabel("Friends Name", family="Arial",fontsize = 20,fontweight="bold",color="black")
plt.ylabel("Income in next year", family="Arial",fontsize = 20,fontweight="bold",color="black")
plt.title("Income of the Hackathon Team")
plt.legend(title="Income of Friends",shadow=True)
plt.annotate(f"Highest Earner is {names_x[np.argmax(income_y)]} with an income of Rs{np.max(income_y):,}", xy=(np.argmax(income_y), np.max(income_y)),xytext=(np.argmax(income_y)+0.2, np.max(income_y)-500), arrowprops=dict(arrowstyle="->", color="gray"),color="black", fontsize=10, family="Arial", fontweight="bold")
plt.grid(axis="both",linewidth=2,color="lightgray",linestyle="dashed")
plt.show()
