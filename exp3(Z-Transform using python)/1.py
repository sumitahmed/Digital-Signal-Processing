#to perform z transform of finite duration non causal signal
import numpy as np
z=np.symbols('z')
indices=[-2,-1,0,1,2]
values=[2,-1,0,3,5]

x_z=0
for i,val in enumerate(values):
    x_z+=val*z**(-indices[i])
x_z_simplified=sp.simplify(x_z)
print("Z transform of the Non-Causal Signal:")
print(x_z_simplified)