# Y[n] += xp[n-k] * hp[k]

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,1]
h = [1,1,1]

N1 = len(x)
N2 = len(h)

N = N1 + N2 - 1

xp = np.zeros(N)
hp = np.zeros(N)

for i in range(N1):
    xp[i] = x[i]

for i in range(N2):
    hp[i] = h[i]


Y = np.zeros(N)

for n in range(N):
    for k in range(N):
        if n>=k:
            Y[n] += xp[n-k] * hp[k]

print("linear convolution without in build bs:",Y)
plt.stem(Y)
plt.grid(True)
plt.show()
