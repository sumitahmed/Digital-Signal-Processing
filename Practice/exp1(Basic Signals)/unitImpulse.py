# del(n) = 1, for n=0, and 0 else where
# relatin bwn del and u(n): del(n) = u(n) - u(n-1)

import numpy as np
import matplotlib.pyplot as plt

n= np.arange(-5, 10)
u = np.where(n== 0,1,0) #assigns value 1, only at n==0, others 0

plt.stem(n,u)
plt.show()