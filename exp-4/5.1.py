from scipy.signal import zpk2tf

z = [-1]
p = [1, 2]
k = 1

b, a = zpk2tf(z, p, k)
print("Numerator coefficients (b):", b)
print("Denominator coefficients (a):", a)
