import numpy as np
rng=np.random.default_rng()
Susans_choice=np.array(['Preeti','Rojina','Isha','Rose','Binita','Manisha','Aashma','Nimu','Jigyasha'])
pick=[]
pick = rng.choice(Susans_choice, size=len(Susans_choice), replace=False)
print(pick)