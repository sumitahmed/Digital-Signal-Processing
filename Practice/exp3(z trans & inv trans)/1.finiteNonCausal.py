# Z-TRANSFORM OF FINITE DURATION NON-CAUSAL SIGNAL
# Signal Type

# Exists for both negative and positive values of n

# Example: n = −2, −1, 0, 1, 2

import numpy as np
import sympy as sp

z = sp.symbols('z')

index = [-2,-1, 0, 1, 2]
values = [2, -1, 0, 3, 5]

Xz =0
for i in range(len(index)):
    Xz = values[i] * z**(-index[i])

print('Z transform',sp.simplify(Xz))