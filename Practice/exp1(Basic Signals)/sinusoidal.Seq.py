#x(n) = Asin(2.PI.f.n + phi)
#A = Amplitue
# PI = np.pi
# f= freq
# phi = phase

import numpy as np
import matplotlib.pyplot as plt

n= np.arange(0,10)
f= 0.25
# phi = np.pi/4

x= np.sin(2*np.pi*f*n)
plt.stem(n,x)
plt.show()