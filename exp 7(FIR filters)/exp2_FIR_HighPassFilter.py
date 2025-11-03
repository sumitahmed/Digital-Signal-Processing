import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz  

# Sampling frequency and cutoff
fs = 1000
fc = 100
numtaps = 101

# Define figure and subplots
fig, ans = plt.subplots(4, 1, figsize=(10, 12))

# Updated valid window names for SciPy
windows = ['hamming', 'hann', 'boxcar', 'bartlett']  # 'hann' replaces 'hanning'

# Loop through each window type
for i, window in enumerate(windows):
    # High-pass FIR filter
    firCoeff = firwin(numtaps, fc, window=window, fs=fs, pass_zero=False)
    w, h = freqz(firCoeff, worN=8000, fs=fs)
    
    ans[i].plot(w, 20 * np.log10(np.abs(h)), label=f'{window.capitalize()} Window')
    ans[i].set_title(f'High Pass Filter Frequency Response using {window.capitalize()} Window')
    ans[i].set_xlabel('Frequency (Hz)')
    ans[i].set_ylabel('Magnitude (dB)')
    ans[i].grid(True)
    ans[i].legend()

# Adjust layout and show plots
plt.tight_layout()
plt.show()
