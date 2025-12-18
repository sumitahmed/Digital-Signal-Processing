# Obtain the transfer function coefficients from the given poles and zeroes.

# Then they will give you something like this:

# • Zeros: z = [-1]
# • Poles: p = [1, 2]
# • Gain: k = 1

import scipy.signal as sc

z = [-1]
p = [1,2]
k = 1

num, den = sc.zpk2tf(z,p,k)

print("num coeff", num)
print("den coeff", den)