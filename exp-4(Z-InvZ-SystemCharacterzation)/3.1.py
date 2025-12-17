#z and inv z using LCAPY
from sympy.abc import n,a
from lcapy.discretetime import n as dn
x_z = a**n
x_z=a**n * dn(n)

print("Z Transform using LCAPY:")
print(x_z.ZT())

