#pole-zero plot and transfer funcion coefficients using scipy and matplotlib
#pole zero plot
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

b=[1,1]
a=[1,-3,2]

z,p,k= tf2zpk(b,a)
plt.figure()
plt.scatter(z.real, z.imag, marker='o', color='blue',label='Zeros')
plt.scatter(p.real, p.imag, marker='o', color='red',label='poles')

plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary') 

plt.title('Pole-Zero Plot')
plt.legend()
plt.grid(True)
plt.show()