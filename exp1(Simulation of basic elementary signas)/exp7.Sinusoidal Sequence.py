import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 9, 1)
f = 1/4  # frequency
y = np.sin(2 * np.pi * f * n)

plt.stem(n, y)
plt.title('Sinusoidal Sequence sin(2πfn)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
