#coeff from rational function
from scipy.signal import tf2zpk
from sympy import symbols, apart
num = [1,2,0]
den = [1.-5,6]
z, p, k = tf2zpk(num, den)
print("Numerator coefficients (num):", num)
print("Denominator coefficients (den):", den)