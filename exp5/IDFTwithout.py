import numpy as np

# Example DFT coefficient sequence
X = [0, 1, 0, 1]
N = len(X)
x_n = np.zeros(N, dtype=complex)
for n in range(N):
    for k in range(N):
        x_n[n] += X[k] * np.exp(2j * np.pi * k * n / N)
x_n = x_n / N

print("IDFT x[n]:", x_n)
