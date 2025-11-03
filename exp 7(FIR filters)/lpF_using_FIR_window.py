#Design Low pass filter using FIR window method
#window method: Hamming window = 'hamming' , Hanning window = 'hanning', rectangular window = 'rectangular', barlett window = 'bartlett'
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

#design a low_pass filter
numtaps = 101
cutoff = 0.3
coefficients = firwin(numtaps, cutoff, window='hamming')

#plot the freq response
w,h = freqz(coefficients)
plt.plot(w/np.pi, 20*np.log10(np.abs(h)))
plt.title('Low Pass Filter Frequency Response using Hamming Window')
plt.xlabel('Normalized Frequency (rad/sample)')
plt.ylabel('Magnitude (dB)')

plt.grid()
plt.show()
