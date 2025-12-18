import matplotlib.pyplot as plt
import numpy as np

Xn = [0,1,0,1]
N = len(Xn)

x = np.zeros(N, dtype=complex)

for n in range(N):
    for k in range(N):
        x+= Xn[k] * np.exp(2j*np.pi*k*n / N)

x=x/N
print("Idft",x)

#time domain
n=np.arange(N)
plt.stem(n,np.real(x))

plt.show()