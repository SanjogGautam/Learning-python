import numpy as np
rng=np.random.default_rng(seed=1)
choice=np.array(['Sunmaya','Rabin','Buddha','Yojana','Mohit','Naw raj','Ishwori','Prajwal'])
hatest=rng.choice(choice, replace=False)
print(f'The Hatest Person of Sudiksyaa Neupane is: {hatest} ')
