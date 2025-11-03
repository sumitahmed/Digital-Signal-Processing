import numpy as np
import matplotlib.pyplot as plt

# Original Signal
t = np.linspace(0, 1, 100)
x = np.sin(2 * np.pi * 5 * t)

# DPCM Encoding and Decoding
Δ = 0.2
x_recon = np.zeros_like(x)
for i in range(1, len(x)):
    pred = x_recon[i-1]
    error = x[i] - pred
    q_error = round(error / Δ) * Δ
    x_recon[i] = pred + q_error

# Plot
plt.plot(t, x, label='Original Signal')
plt.plot(t, x_recon, '--', label='DPCM Reconstructed')
plt.title("DPCM Signal Reconstruction")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
