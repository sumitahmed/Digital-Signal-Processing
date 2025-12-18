#     num = [1, 2, 0]
# den = [1, -5, 6]

import scipy.signal as sc 
import matplotlib.pyplot as plt

num  = [1,2,0]
den = [1, -5, 6]

z,p,k = sc.tf2zpk(num, den)

plt.scatter(z.real, z.imag, label = "zeros")
plt.scatter(p.real, p.imag, label = "poles")

plt.xlabel("real")
plt.ylabel("imag")

plt.legend()
plt.grid(True)
plt.show()