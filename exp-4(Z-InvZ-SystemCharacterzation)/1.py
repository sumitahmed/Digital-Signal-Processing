#inv z using partial fraction
from sympy import sysmbols, apart
z=symbols('z')
FZ= z/((z-1)*(z-2))

partial_frac = apart(FZ,z)
print("Partial Fraction Decomposition of F(z):")
print(partial_frac)