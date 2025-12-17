import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

b = [1, 1]
a = [1, -3, 2]

z, p, k = tf2zpk(b, a)

plt.figure()
plt.scatter(z.real, z.imag, marker='o', color='blue', label='zeros')
plt.scatter(p.real, p.imag, marker='x', color='red', label='poles')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Plot')
plt.legend()
plt.grid(True)
plt.show()
