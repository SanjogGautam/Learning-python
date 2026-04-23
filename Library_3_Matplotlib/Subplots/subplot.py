import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()
Classmates = ["Susan","Swagat","Sanjog","Bibek","Hiro","Sarad","Chuchi","Pritam","Khewang"]

funny_index = rng.integers(1, 100, size=len(Classmates))
handsome_index = rng.integers(1, 100, size=len(Classmates))
figures,axes=plt.subplots(2,2)
axes[0][0].scatter(Classmates, funny_index, color="Blue", alpha=0.5, label="Funny Level")
axes[0][0].scatter(Classmates, handsome_index, color="Red", alpha=0.5, label="Handsome Level")
axes[0][0].set_xlabel("Classmates")
axes[0][0].set_ylabel("Level (1-100)")
axes[0][0].set_title("The Funny-Handsome Matrix")
axes[0][0].legend() 
figures.suptitle("All the plots i have made so far")
# 3. TOP-RIGHT: A Box Plot of the same data
axes[0][1].boxplot([funny_index, handsome_index], labels=["Funny", "Handsome"], patch_artist=True)
axes[0][1].set_title("Distribution Summary")
#pathc_artist is used to fill the box with color
# 4. BOTTOM-LEFT: Maybe a Bar Chart?
axes[1][0].bar(Classmates, funny_index, color="skyblue")
axes[1][0].set_title("Funny Levels per Person")
axes[1][0].tick_params(axis='x', rotation=45)

# 5. BOTTOM-RIGHT: Just a placeholder for now
axes[1][1].text(0.5, 0.5, "Future Analysis", ha='center')#ha is horizontal alignment
axes[1][1].set_title("Coming Soon")
plt.tight_layout() #to avoid overlapping of subplots    
plt.show()
plt.savefig("subplot.png")#it is ued to save the figure in the current working directory with the name subplot.png