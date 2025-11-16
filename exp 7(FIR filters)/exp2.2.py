import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

fs = 1000
fc = 100
numtaps = 101

# Designing High-Pass Filters with different windows
h_w_1 = firwin(numtaps, fc, window='hamming', fs=fs, pass_zero=False)
h_w_2 = firwin(numtaps, fc, window='hann', fs=fs, pass_zero=False)
h_w_3 = firwin(numtaps, fc, window='boxcar', fs=fs, pass_zero=False)
h_w_4 = firwin(numtaps, fc, window='bartlett', fs=fs, pass_zero=False)

# Frequency responses
w1, h1 = freqz(h_w_1)
w2, h2 = freqz(h_w_2)
w3, h3 = freqz(h_w_3)
w4, h4 = freqz(h_w_4)

# Plot all in one 2×2 figure
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(w1/np.pi, 20 * np.log10(abs(h1)))
plt.title('HPF Freq Response (hamming)')
plt.xlabel('Normalized Freq (rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(w2/np.pi, 20 * np.log10(abs(h2)))
plt.title('HPF Freq Response (hann)')
plt.xlabel('Normalized Freq (rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(w3/np.pi, 20 * np.log10(abs(h3)))
plt.title('HPF Freq Response (rectangular)')
plt.xlabel('Normalized Freq (rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(w4/np.pi, 20 * np.log10(abs(h4)))
plt.title('HPF Freq Response (bartlett)')
plt.xlabel('Normalized Freq (rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()

plt.tight_layout()
plt.show()
