import matplotlib.pyplot as plt
import numpy as np

# Generate a mother wavelet (e.g., Morlet)
def morlet_wavelet(t, w=5):
    return np.cos(w * t) * np.exp(-t**2 / 2)

# Create time vector
t = np.linspace(-2, 2, 1000)

# Plot mother wavelet and a few scaled/shifted versions
fig, ax = plt.subplots(figsize=(10, 6))

# Mother wavelet
ax.plot(t, morlet_wavelet(t), label='ψ(t) (Mother Wavelet)', linewidth=2)

# Scaled and shifted versions
scales = [0.5, 1.5]
shifts = [-1, 1]
for a in scales:
    for b in shifts:
        transformed = (1 / np.sqrt(abs(a))) * morlet_wavelet((t - b) / a)
        ax.plot(t, transformed, linestyle='--', label=f'ψ((t - {b})/{a})')

ax.set_title("Mother Wavelet and Scaled/Shifted Versions")
ax.legend(loc='upper right')
ax.grid(True)
plt.tight_layout()
plt.show()
