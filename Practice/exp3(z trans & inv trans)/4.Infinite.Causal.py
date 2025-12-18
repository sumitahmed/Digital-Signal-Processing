# Z-TRANSFORM OF INFINITE DURATION CAUSAL SIGNAL
# X = n*u(n)

import sympy as sp

z,n = sp.symbols('z n')
xn = n

Xz = sp.summation(xn * z**(-n), (n,0,sp.oo))

print(sp.simplify(Xz))