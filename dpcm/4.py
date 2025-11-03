import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 10, 1)
x = np.sin(0.5 * t)  # original signal
x_pred = np.roll(x, 1)  # predicted signal
x_pred[0] = 0
diff = x - x_pred

plt.plot(t, x, label="Original Signal")
plt.plot(t, x_pred, label="Predicted Signal")
plt.stem(t, diff, linefmt='r-', markerfmt='ro', basefmt='r-', label="Difference")
plt.legend()
plt.title("DPCM Encoding: Difference Between Samples")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
