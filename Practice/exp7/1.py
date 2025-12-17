import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

numtaps = 121
cutoff = 0.3

h_hamming = firwin(numtaps, cutoff, window='hamming')
h_hann = firwin(numtaps, cutoff, window='hann')
h_rect = firwin(numtaps, cutoff, window='boxcar')
h_bartlett = firwin(numtaps, cutoff, window='bartlett')

w, H1 = freqz(h_hamming)
_, H2 = freqz(h_hann)
_, H3 = freqz(h_rect)
_, H4 = freqz(h_bartlett)

plt.figure(figsize=(10,8))
plt.subplot(2,2,1); plt.plot(w/np.pi, 20*np.log10(abs(H1))); plt.title("Hamming")
plt.subplot(2,2,2); plt.plot(w/np.pi, 20*np.log10(abs(H2))); plt.title("Hann")
plt.subplot(2,2,3); plt.plot(w/np.pi, 20*np.log10(abs(H3))); plt.title("Rectangular")
plt.subplot(2,2,4); plt.plot(w/np.pi, 20*np.log10(abs(H4))); plt.title("Bartlett")
plt.tight_layout()
plt.show()
