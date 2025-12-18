#ramp: r(n) = n*u(n), ramp signal inceares linearly with time
# for n>=0, o/p = n, for n<0, o/p = 0
import numpy as np
import matplotlib.pyplot as plt

n= np.arange(-5,10)
u= np.where(n>= 0,n,0)

plt.stem(n,u)
plt.show()