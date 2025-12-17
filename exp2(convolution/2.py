# Linear Convolution WITHOUT Using Inbuilt Function
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 1]
h = [1, 1, 1]

N1 = len(x)
N2 = len(h)
N = N1 + N2 - 1

x = np.append(x, np.zeros(N - N1))
h = np.append(h, np.zeros(N - N2))

y = np.zeros(N)

for n in range(N):
    for k in range(N):
        if n >= k:
            y[n] += x[n - k] * h[k]

print("Linear Convolution Output:", y)

plt.stem(y)
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Linear Convolution (Without Inbuilt Function)")
plt.grid(True)
plt.show()
