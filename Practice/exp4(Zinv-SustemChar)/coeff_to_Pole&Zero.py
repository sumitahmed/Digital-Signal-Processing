# Convert transfer function coefficients → poles and zeros

import scipy.signal as sc
num = [1, 2, 0]
den  = [1, -5,6]

z,p,k = sc.tf2zpk(num,den)

print(z)
print(p)
print(k)