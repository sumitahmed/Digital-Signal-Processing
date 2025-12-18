# Z-TRANSFORM OF FINITE DURATION ANTI-CAUSAL SIGNAL
# Exists only for n<0

import sympy as sp

Xz = 0
z = sp.symbols('z')
indices = [-5,-4,-3,-2,-1]
values = [5,3,8,222,1]

for i in range(len(indices)):
    Xz += values[i] * z**(-indices[i])

print(sp.simplify(Xz))
