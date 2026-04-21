#Generates N evenly spaced values between start and stop (inclusive by default). Unlike arange(), you specify the number of points, not the step size.
#np.linspace(start, stop, num, endpoint=True)
import numpy as np
print(np.linspace(1,13,4))#it is inclusive including13
#there is np.logspace for 10^start and stop
print(np.logspace(1,4,4))