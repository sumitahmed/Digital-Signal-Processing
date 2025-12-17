#find poles and zeroes of a tranfer function using scipy 
from scipy import tf2zpk

b=[0.2,0.4,0.6]
a=[1,-1.28,0.57,-0.1]

z,p,k = tf2zpk(b,a)
print("Zeros of the Transfer Function:", z)
print("Poles of the Transfer Function:", p)
print("Gain of the Transfer Function:", k)