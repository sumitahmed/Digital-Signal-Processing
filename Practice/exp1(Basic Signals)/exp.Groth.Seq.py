#Exponentially groth sequence: x(n) = a^n, where a>1
# x(n)=a^n, for n>=0, 
# x(n) = 0, for n<0

import numpy as np
import matplotlib.pyplot as plt

n= np.arange(0,10)
u= np.where(n>= 0, 2**n, 0)

plt.stem(n,u)
plt.show()