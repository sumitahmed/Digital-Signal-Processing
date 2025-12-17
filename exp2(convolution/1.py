import matplotlib.pyplot as plt
import numpy as np

# Define input signals
x = np.array([1, 2, 1])
h = np.array([1, 1])

# Perform linear convolution
y = np.convolve(x, h)

# Create subplots to show flip, shift, multiply, sum
fig, axes = plt.subplots(4, 1, figsize=(10, 10))
n_vals = range(len(y))

# Step 1: Plot x[n]
axes[0].stem(range(len(x)), x, basefmt=" ")
axes[0].set_title("Input Signal x[n]")
axes[0].set_xlim(-1, len(y))
axes[0].grid(True)

# Step 2: Plot flipped h[-k]
h_flipped = h[::-1]
axes[1].stem(range(-len(h_flipped)+1, 1), h_flipped, basefmt=" ")
axes[1].set_title("Flipped Signal h[-k]")
axes[1].set_xlim(-1, len(y))
axes[1].grid(True)

# Step 3: Show shifting and overlapping
for i in range(len(y)):
    axes[2].cla()
    x_range = np.arange(len(x))
    h_shifted = np.zeros_like(x)
    h_start = i - len(h_flipped) + 1
    for j in range(len(h_flipped)):
        if 0 <= h_start + j < len(x):
            h_shifted[h_start + j] = h_flipped[j]
    axes[2].stem(x_range, x, linefmt='b-', markerfmt='bo', basefmt=" ", label='x[n]')
    axes[2].stem(x_range, h_shifted, linefmt='g-', markerfmt='go', basefmt=" ", label='Shifted h[-k+n]')
    axes[2].set_title(f"n = {i}: Shift and Overlap")
    axes[2].legend()
    axes[2].set_xlim(-1, len(y))
    axes[2].grid(True)
    plt.pause(0.5)

# Step 4: Show final result y[n]
axes[3].stem(n_vals, y, basefmt=" ")
axes[3].set_title("Output Signal y[n] = x[n] * h[n]")
axes[3].set_xlim(-1, len(y))
axes[3].grid(True)

plt.tight_layout()
plt.show()
