import numpy as np 
from scipy.signal import firwin, freqz, lfilter
import matplotlib.pyplot as plt

# Sampling and cutoff frequencies
fs = 100           # Sampling frequency (Hz)
fc = 10            # Cutoff frequency (Hz)

# FIR filter design
numtaps = 101      # Number of filter coefficients (taps)
fir_coeff = firwin(numtaps, fc, fs=fs, pass_zero=True)

# Frequency response
w, h = freqz(fir_coeff, worN=8000, fs=fs)
plt.figure(1)
plt.plot(w, 20 * np.log10(np.abs(h)), label='FIR Low Pass Filter')
plt.title('Frequency Response of FIR Low Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend()
plt.grid()
plt.show()

# Generate a noisy signal
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.random(t.size)

# Apply the FIR filter
filtered_signal = lfilter(fir_coeff, 1.0, signal)

# Plot signals
plt.figure(2)
plt.plot(t, signal, 'r', label='Noisy Signal')
plt.plot(t, filtered_signal, 'b', label='Filtered Signal')
plt.title('Signal Before and After FIR Low Pass Filtering')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
