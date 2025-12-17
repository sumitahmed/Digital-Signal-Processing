import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

order = 5
cutoff = 0.3                 # normalized (0..1) of Nyquist

b, a = butter(order, cutoff, btype='low', analog=False)   # boolean False
w, h = freqz(b, a, worN=1024)                             # note the comma

plt.figure(figsize=(10, 6))
plt.plot(w/np.pi, 20*np.log10(np.maximum(np.abs(h), 1e-12)), 'b', lw=2)
plt.xlabel('Normalized frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.title('5th‑order Butterworth Low‑pass (digital)')
plt.grid(True)
plt.show()
