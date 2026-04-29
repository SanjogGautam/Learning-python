import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("bestsellers_with_categories.csv",index_col="Name")
#"Which category is performing best?"
print(df.groupby("Genre")['User Rating'].mean())
#is there correlation between user rating and price?
print(df[["User Rating","Price"]].corr())
#this shows that there is no correlation between user rating and price. We can also visualize this using a scatter plot.
import matplotlib.pyplot as plt
plt.scatter(df["User Rating"],df["Price"])
plt.xlabel("User Rating")
plt.ylabel("Price")
plt.title("Scatter plot of User Rating vs Price")
plt.show()