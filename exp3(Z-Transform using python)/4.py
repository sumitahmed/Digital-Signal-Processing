#z trans of infinite duration causal signal
import numpy as np
z,n = np.symbols('Zn')

x_n  = n 
x_z = sp.summation(x_n*z**(-n),(n,0,sp.oo))
x_z_simplified=sp.simplify(x_z)
print("Z transform of the Causal Signal:")
print(x_z_simplified)