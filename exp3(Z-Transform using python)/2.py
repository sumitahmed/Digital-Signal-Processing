#to perform z transform of finite duration  causal signal
import sympy as sp
Z = sp.Symbol('z')
indices = [0, 1, 2, 3, 4]
values = [3, 2, 1, 0, 4]
x_z = 0

for i,val in enumerate(values):
    x_z+=val*z**(-indices[i])
x_z_simplified=sp.simplify(x_z)
print("Z transform of the Non-Causal Signal:")
print(x_z_simplified)