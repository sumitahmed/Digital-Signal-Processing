#z using LCAPY
from lcapy.discretetime import z 
xz=z/((z-1)*z)
print("Z Transform using LCAPY:")
print(xz.IZT())

