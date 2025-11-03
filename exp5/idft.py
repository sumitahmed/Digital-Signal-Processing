import numpy as np
import matplotlib.pyplot as plt

# Given DFT coefficients
X = [0, 1, 0, 1]

# Compute inverse DFT
x_n = np.fft.ifft(X)
print('IDFT (complex results):', x_n)

# Take the real part only (since imaginary parts are ~0 for real signals)
x_real = np.real(x_n)
print('IDFT (real results):', x_real)

# Plotting
fig = plt.figure()
plt.stem(x_real)
plt.xlabel('n --->')
plt.ylabel('Amplitude')
plt.title('Inverse DFT')
plt.show()
