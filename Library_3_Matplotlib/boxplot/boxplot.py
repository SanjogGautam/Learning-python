import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # Needed for the custom legend

# 1. Setup Data
a = np.random.normal(70, 30, 100).clip(0, 100)
b = np.random.normal(50, 40, 100).clip(0, 100)
c = np.random.normal(90, 50, 100).clip(0, 100)

labels = ["ClassA", "ClassB", "ClassC"]
colors = ["red", "blue", "green"]

# 2. Create the Boxplot
# We save the result in 'bp' so we can access the boxes later
bp = plt.boxplot([a, b, c], labels=labels, patch_artist=True)

# 3. Apply Colors to the Boxes
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5) # Optional: make it a bit transparent

# 4. Create a Manual Legend
# We create "patches" to act as legend handles
handles = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(labels))]
plt.legend(handles=handles, title="Types")

# 5. Formatting
plt.xlabel("Classes")
plt.ylabel("Scores (0-100)")
plt.title("Class Performance Comparison")
plt.show()