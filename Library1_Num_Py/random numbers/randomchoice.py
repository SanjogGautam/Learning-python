import numpy as np
rng=np.random.default_rng()
Susans_choice=np.array(['Preeti','Rojina','Isha','Rose','Binita','Manisha','Aashma','Nimu','Jigyasha'])
pick=[]
pick = rng.choice(Susans_choice, size=len(Susans_choice), replace=False)
#If you are picking a very large number of items without replacement from a huge array, rng.choice(replace=False)
print(pick)