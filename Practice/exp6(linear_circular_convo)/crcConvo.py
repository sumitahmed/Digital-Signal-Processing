# Y[n] += xp[n-k] * hp[k]
# x[n] = [1, 2, 3, 1]
# h[n] = [1, 1, 1]

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,1]
h= [1,1,1]

Lx = len(x)
Lh = len(h)

N = max(Lx,Lh)

xp = np.zeros(N)
hp = np.zeros(N)

for i in range(Lx):
    xp[i] = x[i]
for i in range(Lh):
    hp[i] = h[i]

Y = np.zeros(N)

for n in range(N):
    for k in range(N):
        Y[n]+= xp[n] * hp[(n-k) % N]

print("circular convo:",Y)

plt.stem(Y)
plt.show()