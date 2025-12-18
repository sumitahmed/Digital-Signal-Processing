#N = N1+N2 - 1

import numpy as np

x = [1,2,3,4]
h= [1,1,1]

N1 = len(x)
N2 = len(h)

N = N1+ N2 -1

#zero padding:
xp = np.zeros(N)
hp = np.zeros(N)

for i in range(N1):
    xp[i] = x[i]

for i in range(N2):
    hp[i] = h[i]

print("length after zero padded", N)

print("zero padded x:", xp)
print("zero padded h:", hp)

