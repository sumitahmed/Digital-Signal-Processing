# Linear Convolution Using Zero Padding
import numpy as np

x = np.array([1, 2, 3, 1])
h = np.array([1, 1, 1])

N1 = len(x)
N2 = len(h)
N = N1 + N2 - 1

xp = np.zeros(N)
hp = np.zeros(N)

xp[:N1] = x
hp[:N2] = h

print("Length of x:", N1)
print("Length of h:", N2)
print("Length after zero padding:", N)
print("Zero padded x:", xp)
print("Zero padded h:", hp)
