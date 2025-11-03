import sympy as sp
Z = sp.Symbol('z')
indices = [0, 1, 2, 3, 4]
values = [3, 2, 1, 0, 4]
x_z = sum(val * Z**(-idx) for val, idx in zip(values, indices))
print("Z transform of the Causal Signal:")
print(sp.simplify(x_z))