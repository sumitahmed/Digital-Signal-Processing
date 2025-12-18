#u(n-k) = 1, for n>=k
#u(n-k) = 0, for n<k

import numpy as np
import matplotlib.pyplot as plt

n= np.arange(-5, 10)
u = np.where(n>= 5, 1, 0) #the signal becomes 1 only at n=5, n<5 =0, n>5 =1

plt.stem(n,u)
plt.title("delayed unit step seq")
plt.xlabel("n")
plt.ylabel("amp")
plt.grid(True)
plt.show()