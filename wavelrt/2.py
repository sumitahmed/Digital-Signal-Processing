import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import stft
import pywt

# Generate a sample signal: 3 frequencies in time segments
fs = 500  # Sampling frequency
t = np.linspace(0, 1, fs)
signal = np.concatenate([
    np.sin(2 * np.pi * 5 * t[:fs//3]),         # Low frequency
    np.sin(2 * np.pi * 20 * t[fs//3:2*fs//3]), # Mid frequency
    np.sin(2 * np.pi * 50 * t[2*fs//3:])       # High frequency
])

# --- Plotting ---
fig, axs = plt.subplots(1, 3, figsize=(18, 4))

# 1. Fourier Transform (FT)
fft_vals = np.abs(np.fft.rfft(signal))
fft_freqs = np.fft.rfftfreq(len(signal), 1/fs)
axs[0].plot(fft_freqs, fft_vals)
axs[0].set_title("Fourier Transform (FT)")
axs[0].set_xlabel("Frequency [Hz]")
axs[0].set_ylabel("Amplitude")

# 2. Short-Time Fourier Transform (STFT)
f, t_stft, Zxx = stft(signal, fs=fs, nperseg=64)
axs[1].pcolormesh(t_stft, f, np.abs(Zxx), shading='gouraud')
axs[1].set_title("Short-Time Fourier Transform (STFT)")
axs[1].set_xlabel("Time [s]")
axs[1].set_ylabel("Frequency [Hz]")

# 3. Wavelet Transform (WT)
scales = np.arange(1, 128)
coeffs, freqs = pywt.cwt(signal, scales, 'morl', sampling_period=1/fs)
axs[2].imshow(np.abs(coeffs), extent=[0, 1, freqs[-1], freqs[0]], aspect='auto', cmap='viridis')
axs[2].set_title("Wavelet Transform (WT)")
axs[2].set_xlabel("Time [s]")
axs[2].set_ylabel("Frequency [Hz]")

plt.tight_layout()
plt.show()
