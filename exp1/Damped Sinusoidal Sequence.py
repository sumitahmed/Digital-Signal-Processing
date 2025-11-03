import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 500)
y = np.sin(10 * np.pi * t) * np.exp(-t / 2)

plt.plot(t, y)
plt.title('Damped Sinusoidal y(t) = sin(10πt)·exp(-t/2)')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
