import pandas as pd
df=pd.read_csv("data.csv",index_col="Name")
tall_pokemon=df[df["Height"]>=2]
print(tall_pokemon)
grass_type=df[(df["Type1"]=="Grass") | (df["Type2"]=="Grass")]
print (grass_type)
grass_poison=df[(df["Type1"]=="Grass") & (df["Type2"]=="Poison")]
print(grass_poison)