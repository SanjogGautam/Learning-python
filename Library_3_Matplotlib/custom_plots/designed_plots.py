import matplotlib.pyplot as plt
import numpy as np
#markers are the data points on the axis
#lines are the line connecting the points
x=np.array([2023,2024,2025,2026])
y1=np.array([15,20,30,10])
y2=np.array([17,23,38,5])
style=dict(marker="o",markersize=10,markerfacecolor="red",markeredgecolor="red",linestyle="solid",color="green",linewidth=4)
#plt.plot(x,y1,marker="o",makersize=25,markerfacecolor="red",markeredgecolor="red",linestyle="solid",color="green",linewidth=4)#it is by default solid
#instead of deeining the list individually we can define the list as above
plt.plot(x,y1,**style)
plt.plot(x,y2,**(style | {"color":"yellow","markerfacecolor":"aqua","markeredgecolor":"aqua"}))#**style is we are unpacking the data this method is used to change the color of the second line to yellow
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend(["Product 1","Product 2"])
plt.title("Sales of products over years")
plt.show()