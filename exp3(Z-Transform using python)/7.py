#inverse z
import sympy as np
import matplotlib.pyplot as plt
coeff = [1,0,-1,3]
N= len(coeff)
sequence = np.Array(coeff)
n= np.arrange(N)

plt.stem(n,sequence)
plt.title('Inverse Z-transform of X(z) = 1 - z^-2 + 3z^-3')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()

