import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
Classmates = ["Susan","Swagat","Sanjog","Bibek","Hiro","Sarad","Chuchi","Pritam","Khewang"]

# Generate all 9 numbers at once
funny_index = rng.integers(1, 100, size=len(Classmates))
handsome_index = rng.integers(1, 100, size=len(Classmates))

plt.scatter(Classmates, funny_index, color="Blue", alpha=0.5, label="Funny Level")
plt.scatter(Classmates, handsome_index, color="Red", alpha=0.5, label="Handsome Level")

plt.xlabel("Classmates")
plt.ylabel("Level (1-100)")
plt.title("The Funny-Handsome Matrix")
plt.xticks(Classmates) 
plt.legend()

plt.show()