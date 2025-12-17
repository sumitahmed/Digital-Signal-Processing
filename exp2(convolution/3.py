import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 1]
h = [1, 1, 1]

y = np.convolve(x, h)

print("Linear Convolution Output:", y)

plt.subplot(3, 1, 1)
plt.stem(x)
plt.title("Input Signal x(n)")

plt.subplot(3, 1, 2)
plt.stem(h)
plt.title("Impulse Response h(n)")

plt.subplot(3, 1, 3)
plt.stem(y)
plt.title("Output Signal y(n)")

plt.tight_layout()
plt.show()
