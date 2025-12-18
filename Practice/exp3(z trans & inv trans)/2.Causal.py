# Z-TRANSFORM OF FINITE DURATION CAUSAL SIGNAL

import sympy as sp

indices = [0,1,2,3,4]
values  = [1,2,3,8,11]

z = sp.simplify('z')
Xz=0
for i in range(len(indices)):
    Xz = values[i]*z**(-indices[i])

print(sp.simplify(Xz))
