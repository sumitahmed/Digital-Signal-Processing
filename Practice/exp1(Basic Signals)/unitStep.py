# u(n) = 1 for n>=0 
# u(n) = 0 for n<0

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 10) #cretes discrete time indices
u = np.where(n>= 0,1,0) #implements the unit step definition

plt.stem(n,u)
plt.title("unit step seq")
plt.xlabel("n")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()