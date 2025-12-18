#Damped Sinusoidal signal
#x(n) = sin(w.t) * e^-(at)

import matplotlib.pyplot as plt
import numpy as np

t= np.linspace(0,5,500)
x = np.sin(10*np.pi*t) * np.exp(-2*t)

plt.plot(t,x)
plt.show()