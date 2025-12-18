# x[k] += x[n] * np.exp(-2j * np.pi * k * n/N)

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2,3,4]
N = len(x)

Xn = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        Xn[k] += x[n] * np.exp(-2j * np.pi * k * n /N)

print("dft:",Xn)

print("magnitude", np.abs(Xn))
print("phase", np.angle(Xn))

#mag spectrum
k = np.arange(N)
plt.stem(k,np.abs(Xn))

plt.show()