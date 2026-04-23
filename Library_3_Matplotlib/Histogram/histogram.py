import matplotlib.pyplot as plt
import numpy as np
#it is a visual representation of distribuition of quantitative data
scores=np.random.normal(loc=60,scale=50,size=100)
scores=np.clip(scores,0,100)#doing it so that the scores don't deviate out of 0 to 100
plt.hist(scores,bins=10,color="green",edgecolor="black")
plt.xlabel("Marks")
plt.title("Score Distribution")
plt.ylabel("No of students")
plt.legend()
plt.show()