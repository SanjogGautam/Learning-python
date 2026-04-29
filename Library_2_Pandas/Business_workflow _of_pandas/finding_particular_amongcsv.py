import pandas as pd
#User Rating below 4.0 AND fewer than 1000 reviews.
df=pd.read_csv("bestsellers_with_categories.csv")
print(df[(df["User Rating"]<4.0) & (df["Reviews"]<1000)])
#User Rating above 4.5 OR more than 5000 reviews.
print(df[(df["User Rating"]>4.5) | (df["Reviews"]>5000)])