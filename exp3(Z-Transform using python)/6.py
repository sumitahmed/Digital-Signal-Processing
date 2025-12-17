#to perform z transform of the sequence x[n] =-b^n u[-n-1]
import sympy as sp
z,n,b= sp.symbols('z n b')
x_n = -b**n
x_z = sp.summation(x_n*z**(-n-1),(n,-1,sp.oo))
x_z_simplified= sp.simplify(x_z)
print("Z transform of the sequence x[n] =-b^n u[-n-1]:")
print(x_z_simplified)