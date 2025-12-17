#inv z using partial fraction
from scipy import symbols, apart, expand 
Z = symbols('z')
N= z**2 + 3*z +2
D= z**2 - (3*z)/2 + 1/2
X = N/D
x_apart = apart(X,Z)

x_expanded = expand(x_apart)
print("Inverse Z-transform using Partial Fraction Decomposition:")
print(x_apart)
print("Expanded form:")
print(x_expanded)
