import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

numtaps = 101
cutoff = 0.3
windows = ['hamming', 'hann', 'boxcar', 'bartlett']  # corrected window names

fig, ans = plt.subplots(len(windows), 1, figsize=(8, 12))

for i, window in enumerate(windows):
    coeff = firwin(numtaps, cutoff, window=window)
    w, h = freqz(coeff)
    ans[i].plot(w / np.pi, 20 * np.log10(np.abs(h)))
    ans[i].set_title(f'Low Pass Filter Frequency Response using {window.capitalize()} Window')
    ans[i].set_xlabel('Normalized Frequency (×π rad/sample)')
    ans[i].set_ylabel('Magnitude (dB)')
    ans[i].grid(True)

plt.tight_layout()
plt.show()
