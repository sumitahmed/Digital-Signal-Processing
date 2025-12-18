#Exponential decay signal, x(n) = a^n, where a<1;
# x(n) = a^n, for n>=0
# x(n) = 0, for n<0

import matplotlib.pyplot as plt
import numpy as np
n= np.arange(0,10)

a= 0.9**n
u = np.where(n>= 0,a,0)

plt.stem(n,u)
plt.show()