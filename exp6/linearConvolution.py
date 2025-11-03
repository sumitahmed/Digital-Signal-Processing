import numpy as np
import matplotlib.pyplot as plt  # kept to match the note header; not used

# Inputs exactly as shown
xn = [1, 2, 3, 1]
hn = [1, 1, 1]

# Lengths
lxn = len(xn)
lhn = len(hn)
M= lxn+lhn -1;

# Zero-padding to M = max(lxn, lhn)
xn = np.pad(xn, (0, M - lxn))
hn = np.pad(hn, (0, M - lhn))

# Matrix container (note: zeros not "zeroes", and dtype comma)
xn_lxn = np.zeros((M, M), dtype=int)

# Build matrix: each column is hn circularly rolled by i
for i in range(M):
    xn_lxn[:, i] = np.roll(hn, i)

# Multiply to get output
print(xn_lxn)
y = np.dot(xn_lxn, xn)
print(y)
