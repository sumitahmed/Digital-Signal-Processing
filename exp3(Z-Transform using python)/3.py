#to perform z transform of finite duration anti causal signal
import numpy as np
z=np.symbols('z')
indices=[-5,-4,-3, 2,-1]
values=[2,-1,0,3,5]

x_z=0
for i,val in enumerate(values):
    x_z+=val*z**(-indices[i])
x_z_simplified=sp.simplify(x_z)
print("Z transform of the Non-Causal Signal:")
print(x_z_simplified)