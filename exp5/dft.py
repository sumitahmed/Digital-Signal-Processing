import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt

# Input from user
x = eval(input('Enter the input sequence x[k]: '))
n = int(input('Enter value of n: '))

# Compute DFT
X = fft(x, n)

# Print Discrete Fourier Transform
print('Discrete Fourier Transform X[k] =', X)

# Magnitude response
X_mag_res = abs(X)
print('Magnitude response |X(k)| =', X_mag_res)

# Phase response
X_phase_res = np.angle(X)
print('Phase response <X(k) =', X_phase_res)

# Plotting
k = np.arange(0, n, 1)

plt.figure()
plt.stem(k, X_mag_res, linefmt='grey', markerfmt='o', basefmt='k')
plt.xlabel('Discrete frequency variable k ->')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.title('Magnitude Response')

plt.figure()
plt.stem(k, X_phase_res, linefmt='grey', markerfmt='o', basefmt='k')
plt.xlabel('Discrete frequency variable k ->')
plt.ylabel('Phase (radians)')
plt.grid(True, which='both')
plt.title('Phase Response')
plt.show()
