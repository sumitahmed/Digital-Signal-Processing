import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 10, 1)
y = (0.9) ** n

plt.stem(n, y)
plt.title('Exponential Decay Sequence (0.9^n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
