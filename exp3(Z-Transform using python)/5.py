#to perform z transform of the sequence x[n] = a^n u[n]
import sympy as np
z,n,a= np.symbols('z n a')
x_n = a**n
x_z = np.summation(x_n*z**(-n),(n,0,np.oo))
x_z_simplified= np.simplify(x_z)    
print("Z transform of the sequence x[n] = a^n u[n]:")
print(x_z_simplified)