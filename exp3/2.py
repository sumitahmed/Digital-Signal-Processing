import numpy as np
import matplotlib.pyplot as plt

# Coefficients of z^-n
coeff = [1, 0, -1, 3]
N = len(coeff)

# Sequence
sequence = np.array(coeff)
n = np.arange(N)

# Plot
plt.stem(n, sequence)
plt.title('Inverse Z-transform of X(z) = 1 - z^-2 + 3z^-3')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()
