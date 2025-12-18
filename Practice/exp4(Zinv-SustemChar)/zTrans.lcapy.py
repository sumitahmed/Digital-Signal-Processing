from sympy.abc import n, a
from lcapy.discretetime import n as dn

x = a**n * dn(n)
print(x.ZT())
