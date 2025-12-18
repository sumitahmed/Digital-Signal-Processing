# find poles and zeores of: 
#     num = [1, 2, 0]
# den = [1, -5, 6]

import scipy.signal as sc

num = [1,2,0]
den = [1, -5, 6]

z,p,k = sc.tf2zpk(num, den)

print("poles:",p)
print("zeroes:",z)