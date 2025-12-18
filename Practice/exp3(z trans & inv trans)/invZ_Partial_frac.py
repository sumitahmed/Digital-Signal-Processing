# X(z) = (z² + 3z + 2) / (z² − 1.5z + 0.5)

import sympy as sp
z = sp.symbols('z')
Xz = (z**2 + 3*z + 2) / (z**2 - 1.5*z + 0.5)

print(sp.apart(Xz,z))


