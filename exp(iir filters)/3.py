import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# specs from notes (edit as needed)
# passband: 20–50 Hz with 3 dB ripple, stopband: 14–60 Hz with 40 dB attenuation
wp = [2*np.pi*20, 2*np.pi*50]   # rad/s
ws = [2*np.pi*14, 2*np.pi*60]   # rad/s
gpass, gstop = 3, 40            # dB

# order and critical frequencies (analog band-pass)
N, Wn = signal.buttord(wp, ws, gpass, gstop, analog=True)
print(f"Order and critical freqs: N = {N}, Wn (Hz) = {[w/(2*np.pi) for w in np.atleast_1d(Wn)]}")

# design and plot response
b, a = signal.butter(N, Wn, btype='band', analog=True)

f = np.logspace(1, 3, 500)      # 10 Hz to 1 kHz
w = 2*np.pi*f
_, H = signal.freqs(b, a, w)

plt.semilogx(f, 20*np.log10(np.abs(H)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Butterworth Band‑pass from buttord (analog)')
plt.grid(which='both', axis='both')
plt.show()
