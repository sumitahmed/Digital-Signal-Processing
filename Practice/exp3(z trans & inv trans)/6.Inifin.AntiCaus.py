import sympy as sp

z, n, b = sp.symbols('z n b')
x_n = -b**n

Xz = sp.summation(x_n * z**(-n-1), (n, -1, sp.oo))
print("Z-transform:", sp.simplify(Xz))
