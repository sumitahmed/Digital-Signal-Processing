import numpy as np

# Input sequence and parameters
x_n2 = eval(input('Enter input sequence x[n]: '))
n = int(input('Enter value of n: '))

# Manual DFT calculation without fft
if n > 1:
    Xn = np.zeros(n, dtype=complex)
    for k in range(n):
        for nn in range(n):
            Xn[k] += x_n2[nn] * np.exp(-2j * np.pi * k * nn / n)
else:
    Xn = np.array(x_n2, dtype=complex)

print('Discrete Fourier Transform X[k] =', Xn)

# Display magnitude and phase separately if needed
print('Magnitude |X[k]| =', np.abs(Xn))
print('Phase ∠X[k] (radians) =', np.angle(Xn))
