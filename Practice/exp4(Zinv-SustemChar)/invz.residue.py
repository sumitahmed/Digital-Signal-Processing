from sympy import symbols, residue, simplify

z, n = symbols('z n')
Fz = z / ((z - 1)*(z - 2)*(z - 3))
Gz = Fz * z**(n - 1)

poles = [1, 2, 3]
x_n = sum(residue(Gz, z, p) for p in poles)

print("Inverse Z-transform:", simplify(x_n))
