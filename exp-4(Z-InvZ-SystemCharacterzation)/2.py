#inv z using cauchy residue
from sympy import symbols, residue, simplify
z,n = symbols('z n')
Fz= z/((z-1)*(z-2)*(z-3))
Gz= Fz*z**(n-1)

poles = [1, 2, 3]
x_n = sum(residue(Gz, z, pole) for pole in poles)
fn=simplify(sum(residues))
print("Inverse Z-transform using Cauchy Residue Theorem:")
print("F[n]",fn)