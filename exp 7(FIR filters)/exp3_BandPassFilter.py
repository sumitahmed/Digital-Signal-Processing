import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

fs = 1000
lowCutOff = 100
highCutOff = 300
numtaps = 101
firCoeff= firwin (numtaps, [lowCutOff, highCutOff], pass_zero=False, fs=fs)
w,h = freqz(firCoeff, worN=8000, fs=fs)
plt.figure(figsize=(10,0))
plt.plot(w/np.pi, 20*np.log10(np.abs(h)))
label = ('FIR Bandpass Filtre')

plt.xlabel('Freqz HZ')
plt.ylabel('Magnitude dB')

plt.grid()
plt.legend()
plt.show()