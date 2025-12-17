import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# choose band edges around 2000 Hz (edit to match your spec)
f_low  = 1500.0  # Hz
f_high = 2500.0  # Hz
w1, w2 = 2*np.pi*f_low, 2*np.pi*f_high  # rad/s

# design Chebyshev Type-II (analog)
b10, a10 = signal.iirfilter(10, [w1, w2], rs=60, btype='band',
                            analog=True, ftype='cheby2')
b17, a17 = signal.iirfilter(17, [w1, w2], rs=60, btype='band',
                            analog=True, ftype='cheby2')

# analog frequency grid (Hz -> rad/s)
f = np.logspace(2, 4, 1000)           # 100 Hz to 10 kHz
w = 2*np.pi*f                          # rad/s

# frequency responses (analog)
_, H10 = signal.freqs(b10, a10, w)
_, H17 = signal.freqs(b17, a17, w)

# plot
plt.figure(figsize=(10, 6))
plt.semilogx(f, 20*np.log10(np.abs(H10)), label='Order 10')
plt.semilogx(f, 20*np.log10(np.abs(H17)), label='Order 17')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Chebyshev‑II Band‑pass (analog)')
plt.grid(which='both', axis='both')
plt.legend()
plt.show()
