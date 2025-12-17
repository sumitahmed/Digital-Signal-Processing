import numpy as np
import matplotlib.pyplot as plt

# Define range of n
n = np.arange(-5, 10, 1)  # from -5 to 9

# Delayed unit step u(n-5)
y = np.where(n >= 5, 1, 0)

# Plot
plt.stem(n, y)
plt.title('Delayed Unit Step Sequence u(n-5)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
