import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 10, 1)
y = np.where(n >= 0, n, 0)

plt.stem(n, y)
plt.title('Unit Ramp Sequence r(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
