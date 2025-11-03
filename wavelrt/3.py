import matplotlib.pyplot as plt
import pywt
import numpy as np

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
axs = axs.ravel()

# 1. Haar (Discrete)
wavelet_haar = pywt.Wavelet('haar')
phi, psi, x = wavelet_haar.wavefun(level=5)
axs[0].plot(x, psi)
axs[0].set_title("Haar (Discrete)")

# 2. Daubechies (Discrete, db4)
wavelet_db4 = pywt.Wavelet('db4')
phi, psi, x = wavelet_db4.wavefun(level=5)
axs[1].plot(x, psi)
axs[1].set_title("Daubechies db4 (Discrete)")

# 3. Morlet (Continuous)
wavelet_morl = pywt.ContinuousWavelet('morl')
psi, x = wavelet_morl.wavefun()
axs[2].plot(x, psi)
axs[2].set_title("Morlet (Continuous)")

# 4. Mexican Hat (Continuous)
wavelet_mexh = pywt.ContinuousWavelet('mexh')
psi, x = wavelet_mexh.wavefun()
axs[3].plot(x, psi)
axs[3].set_title("Mexican Hat (Continuous)")

# Formatting
for ax in axs:
    ax.grid(True)
    ax.set_xlim([-1, 1])

plt.suptitle("Common Wavelet Functions", fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
