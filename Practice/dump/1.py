# u(n) = 1, for n>=0, u(n) = 0, for n<0

import numpy as np 
import matplotlib.pyplot as plt
n = np.arange(-5,10)
u = np.where(n>= 0,1,0)

plt.stem(n,u)
plt.show()