import sympy as sp

z, n, a = sp.symbols('z n a')
x_n = a**n

Xz = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
print("Z-transform:", sp.simplify(Xz))
