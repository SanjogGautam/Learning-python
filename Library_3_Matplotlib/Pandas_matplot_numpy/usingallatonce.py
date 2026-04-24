import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('data.csv')
count=df["Type1"].value_counts(ascending=True)#it counts the total values of each types in type1
print(count)#count becomes a series
colors=["Red","blue","green"]
plt.bar(count.index,count.values,color=colors,label="types")
plt.title("Type count of the pokemns")
plt.xlabel("Types of the pokemons")
plt.xticks(rotation=30)
plt.ylabel("Counts of Pokemons")
plt.legend(title="Types of Pokemons",fontsize=12,shadow=True)
plt.tight_layout()#It manages the congestion
plt.show()
