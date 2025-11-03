import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
x = np.sin(2 * np.pi * 5 * t)  # Original signal

x_recon = np.zeros_like(x)
Δ = 0.2  # Step size
for i in range(1, len(x)):
    pred = x_recon[i-1]
    error = x[i] - pred
    q_error = round(error / Δ) * Δ
    x_recon[i] = pred + q_error

plt.plot(t, x, label='Original')
plt.plot(t, x_recon, '--', label='Reconstructed')
plt.title("DPCM Reconstruction")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
